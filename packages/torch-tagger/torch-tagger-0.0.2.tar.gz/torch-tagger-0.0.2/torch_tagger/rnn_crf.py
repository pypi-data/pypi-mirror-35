# -*- coding: utf-8 -*-
# Based https://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html
# Modified by InfinityFuture

import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim

from torch_tagger.utils import START_TAG, STOP_TAG, DEVICE, sequence_mask

def argmax(vec):
    # return the argmax as a python int
    _, idx = torch.max(vec, 1)
    return idx.item()

# Compute log sum exp in a numerically stable way for the forward algorithm
def log_sum_exp(vec):
    max_score = vec[0, argmax(vec)]
    max_score_broadcast = max_score.view(1, -1).expand(1, vec.size()[1])
    t = vec - max_score_broadcast
    t = torch.exp(t)
    t = torch.sum(t)
    t = torch.log(t)
    t = max_score + t
    return t

def argmax_batch(vec):
    # return the argmax as a python int
    _, idx = torch.max(vec, 1)
    return idx

def log_sum_exp_batch(vec):
    batch_size = vec.size()[0]
    amax = argmax_batch(vec)
    max_score = vec.gather(1, amax.view(-1, 1))
    max_score = max_score.view(1, -1)
    max_score_broadcast = max_score.view(batch_size, -1)
    max_score_broadcast = max_score_broadcast.expand(batch_size, vec.size()[1])
    t = vec - max_score_broadcast
    t = torch.exp(t)
    t = torch.sum(t, -1)
    t = torch.log(t)
    t = max_score + t        
    return t[0]


class RNN_CRF(nn.Module):

    def __init__(
        self,
        vocab_size,
        tag_to_ix,
        embedding_dim,
        hidden_dim,
        num_layers=1,
        bidirectional=True,
        embedding_dropout_p=0.1,
        rnn_dropout_p=0.1,
        rnn_type='lstm',
        device=DEVICE
        ):
        super(RNN_CRF, self).__init__()
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.vocab_size = vocab_size
        self.tag_to_ix = tag_to_ix
        self.tagset_size = len(tag_to_ix)
        self.num_layers = num_layers
        self.bidirectional = bidirectional
        self.embedding_dropout_p = embedding_dropout_p
        self.rnn_dropout_p = rnn_dropout_p
        self.device = device
        self.rnn_type = rnn_type

        self.word_embeds = nn.Embedding(vocab_size, embedding_dim)
        if rnn_type == 'lstm':
            self.rnn = nn.LSTM(
                embedding_dim,
                hidden_dim,
                num_layers=num_layers,
                bidirectional=bidirectional
            )
        elif rnn_type == 'gru':
            self.rnn = nn.GRU(
                embedding_dim,
                hidden_dim,
                num_layers=num_layers,
                bidirectional=bidirectional
            )
        else:
            raise Exception('Invalid rnn_type')

        self.embedding_dropout = nn.Dropout(self.embedding_dropout_p)
        self.rnn_dropout = nn.Dropout(self.rnn_dropout_p)

        # Maps the output of the LSTM into tag space.
        self.hidden2tag = nn.Linear(
            hidden_dim * 2 if bidirectional else hidden_dim,
            self.tagset_size
        )

        # Matrix of transition parameters.  Entry i,j is the score of
        # transitioning *to* i *from* j.
        self.transitions = nn.Parameter(
            torch.randn(self.tagset_size, self.tagset_size))

        # These two statements enforce the constraint that we never transfer
        # to the start tag and we never transfer from the stop tag
        self.transitions.data[tag_to_ix[START_TAG], :] = -10000
        self.transitions.data[:, tag_to_ix[STOP_TAG]] = -10000

        # self.hidden = self.init_hidden()

    def init_hidden(self, batch_size):
        bidirectional = self.bidirectional
        hidden_dim = self.hidden_dim
        num_layers = self.num_layers
        rnn_type = self.rnn_type
        if rnn_type == 'lstm':
            return (
                torch.randn(
                    2 * num_layers if bidirectional else num_layers,
                    batch_size,
                    hidden_dim
                ).to(self.device),
                torch.randn(
                    2 * num_layers if bidirectional else num_layers,
                    batch_size,
                    hidden_dim
                ).to(self.device),
            )
        elif rnn_type == 'gru':
            return torch.randn(
                2 * num_layers if bidirectional else num_layers,
                batch_size,
                hidden_dim
            ).to(self.device)

    def _forward_alg(self, feats_batch, lengths_batch):
        # feats_batch dim: [batch_size, seq_len, target_dim]
        # lengths_batch dim: [batch_size]
        batch_size = feats_batch.size()[0]
        alpha_batch = []
        # Do the forward algorithm to compute the partition function
        init_alphas = torch.full((batch_size, self.tagset_size), -10000.).to(self.device)
        # START_TAG has all of the score.
        init_alphas[:, self.tag_to_ix[START_TAG]] = 0.

        for i in range(batch_size):
            feats = feats_batch[i]
            lengths = lengths_batch[i]

            # Wrap in a variable so that we will get automatic backprop
            forward_var = init_alphas[i]

            # Iterate through the sentence
            for feat in feats[:lengths]:
                alphas_t = []  # The forward tensors at this timestep
                for next_tag in range(self.tagset_size):
                    # broadcast the emission score: it is the same regardless of
                    # the previous tag
                    emit_score = feat[next_tag].view(
                        1, -1).expand(1, self.tagset_size)
                    # the ith entry of trans_score is the score of transitioning to
                    # next_tag from i
                    trans_score = self.transitions[next_tag].view(1, -1)
                    # The ith entry of next_tag_var is the value for the
                    # edge (i -> next_tag) before we do log-sum-exp
                    next_tag_var = forward_var + trans_score + emit_score
                    # The forward variable for this tag is log-sum-exp of all the
                    # scores.
                    alphas_t.append(log_sum_exp(next_tag_var).view(1))
                forward_var = torch.cat(alphas_t).view(1, -1)
                # print('forward_var AAA', forward_var.size())
            terminal_var = forward_var + self.transitions[self.tag_to_ix[STOP_TAG]]
            alpha = log_sum_exp(terminal_var)
            alpha_batch.append(alpha)
        return torch.stack(alpha_batch) / lengths.float()
    
    def _forward_alg_batch(self, feats, lengths, masks):
        # feats dim: [batch_size, seq_len, target_dim]
        # lengths dim: [batch_size]
        # masks dim: [batch_size, seq_len]
        batch_size, seq_len = feats.size()[:2]
        # Do the forward algorithm to compute the partition function
        init_alphas = torch.full((batch_size, self.tagset_size), -10000.).to(self.device)
        # START_TAG has all of the score.
        init_alphas[:, self.tag_to_ix[START_TAG]] = 0.

        # Wrap in a variable so that we will get automatic backprop
        forward_var = init_alphas

        # feats dim: [seq_len, batch_size, target_dim]
        feats = feats.permute(1, 0, 2)
        # Iterate through the sentence
        for i, feat in enumerate(feats):
            alphas_t = []  # The forward tensors at this timestep
            for next_tag in range(self.tagset_size):
                # broadcast the emission score: it is the same regardless of
                # the previous tag
                emit_score = feat[:, next_tag].view(
                    batch_size, -1).expand(batch_size, self.tagset_size)
                # the ith entry of trans_score is the score of transitioning to
                # next_tag from i
                trans_score = self.transitions[next_tag].view(1, -1).expand(
                    batch_size, self.tagset_size)
                trans_score = trans_score * masks[:, i]
                # The ith entry of trans_score is the value for the
                # edge (i -> next_tag) before we do log-sum-exp
                next_tag_var = forward_var + trans_score + emit_score
                # The forward variable for this tag is log-sum-exp of all the
                # scores.
                alphas_t.append(log_sum_exp_batch(next_tag_var))
            forward_var = torch.stack(alphas_t)
            forward_var = forward_var.permute(1, 0)
        terminal_var = forward_var + self.transitions[self.tag_to_ix[STOP_TAG]]
        alpha = log_sum_exp_batch(terminal_var) / lengths.float()
        return alpha

    def _get_rnn_features(self, sentence):
        # sentence dim: [batch_size, seq_len]
        batch_size, _ = sentence.size()

        self.hidden = self.init_hidden(batch_size)

        # embeds dim: [batch_size, seq_len, embedding_size]
        embeds = self.word_embeds(sentence)
        embeds = self.embedding_dropout(embeds)
        # embeds dim: [seq_len, batch_size, embedding_size]
        # embeds = embeds.view(seq_len, batch_size, -1)
        embeds = embeds.permute(1, 0, 2)

        # rnn_out dim: [seq_len, batch_size, hidden_dim]
        rnn_out, self.hidden = self.rnn(embeds, self.hidden)
        # When your batch_size > 1, you should use permute not view
        # rnn_out = rnn_out.view(batch_size, seq_len, self.hidden_dim)
        rnn_out = rnn_out.permute(1, 0, 2)
        # rnn_feats dim: [batch_size, seq_len, target_dim]
        rnn_feats = self.hidden2tag(rnn_out)

        return rnn_feats

    def _score_sentence(self, feats_batch, tags_batch, lengths_batch):
        # Gives the score of a provided tag sequence
        # feats_batch dim: [batch_size, seq_len, target_dim]
        # tags_batch dim: [batch_size, seq_len]
        # lengths_batch dim: [batch_size]
        batch_size = feats_batch.size()[0]
        score_batch = []
        for i in range(batch_size):
            score = torch.zeros(1).to(self.device)
            feats = feats_batch[i]
            tags = tags_batch[i]
            lengths = lengths_batch[i]

            tags = torch.cat([
                torch.tensor([self.tag_to_ix[START_TAG]], dtype=torch.long).to(self.device),
                tags
            ])
            
            for j, feat in enumerate(feats):
                score = score + \
                    self.transitions[tags[j + 1], tags[j]] + feat[tags[j + 1]]
            score = score + self.transitions[self.tag_to_ix[STOP_TAG], tags[-1]]
            score = score / lengths.float()
            score_batch.append(score)
        return torch.cat(score_batch)

    def _score_sentence_batch(self, feats, tags, lengths, masks):
        # Gives the score of a provided tag sequence
        # feats dim: [batch_size, seq_len, target_dim]
        # tags dim: [batch_size, seq_len]
        # lengths dim: [batch_size]
        # masks dim: [batch_size, seq_len]
        batch_size = feats.size()[0]

        score = torch.zeros(batch_size).to(self.device)

        start = torch.tensor([
            self.tag_to_ix[START_TAG]
        ], dtype=torch.long).expand(batch_size, 1).to(self.device)

        tags = torch.cat([
            start,
            tags
        ], dim=1)
        
        feats = feats.permute(1, 0, 2)
        for j, feat in enumerate(feats):
            aa, bb = tags[:, j + 1], tags[:, j]
            a = self.transitions[aa, bb]
            a = a * masks[:, j, 0].view(-1)
            b = feat[:, aa]
            score = score + a + b
                
        score = score + self.transitions[self.tag_to_ix[STOP_TAG], tags[:, -1]]
        score = score / lengths.float()

        return score.diag()

    def _viterbi_decode(self, feats_batch):
        # feats_batch dim: [batch_size, seq_len, target_dim]
        batch_size = feats_batch.size()[0]
        path_scores, best_paths = [], []
        for i in range(batch_size):
            feats = feats_batch[i]
            backpointers = []

            # Initialize the viterbi variables in log space
            init_vvars = torch.full((1, self.tagset_size), -10000.).to(self.device)
            init_vvars[0][self.tag_to_ix[START_TAG]] = 0

            # forward_var at step i holds the viterbi variables for step i-1
            forward_var = init_vvars
            for feat in feats:
                bptrs_t = []  # holds the backpointers for this step
                viterbivars_t = []  # holds the viterbi variables for this step

                for next_tag in range(self.tagset_size):
                    # next_tag_var[i] holds the viterbi variable for tag i at the
                    # previous step, plus the score of transitioning
                    # from tag i to next_tag.
                    # We don't include the emission scores here because the max
                    # does not depend on them (we add them in below)
                    next_tag_var = forward_var + self.transitions[next_tag]
                    best_tag_id = argmax(next_tag_var)
                    bptrs_t.append(best_tag_id)
                    viterbivars_t.append(next_tag_var[0][best_tag_id].view(1))
                # Now add in the emission scores, and assign forward_var to the set
                # of viterbi variables we just computed
                forward_var = (torch.cat(viterbivars_t) + feat).view(1, -1)
                backpointers.append(bptrs_t)

            # Transition to STOP_TAG
            terminal_var = forward_var + self.transitions[self.tag_to_ix[STOP_TAG]]
            best_tag_id = argmax(terminal_var)
            path_score = terminal_var[0][best_tag_id]

            # Follow the back pointers to decode the best path.
            best_path = [best_tag_id]
            for bptrs_t in reversed(backpointers):
                best_tag_id = bptrs_t[best_tag_id]
                best_path.append(best_tag_id)
            # Pop off the start tag (we dont want to return that to the caller)
            start = best_path.pop()
            assert start == self.tag_to_ix[START_TAG]  # Sanity check
            best_path.reverse()

            path_scores.append(path_score)
            best_paths.append(best_path)

        return path_scores, best_paths

    def neg_log_likelihood(self, sentence, tags, lengths):
            
        rnn_feats = self._get_rnn_features(sentence)
        batch_size, seq_len, tagset_size = rnn_feats.size()

        masks = sequence_mask(lengths)
        masks = masks.view(batch_size, seq_len, 1)
        masks = masks.expand(batch_size, seq_len, tagset_size)
        rnn_feats = rnn_feats * masks

        rnn_feats = self.rnn_dropout(rnn_feats)

        # forward_score = self._forward_alg(rnn_feats, lengths)
        forward_score = self._forward_alg_batch(rnn_feats, lengths, masks)
        # gold_score = self._score_sentence(rnn_feats, tags, lengths)
        gold_score = self._score_sentence_batch(rnn_feats, tags, lengths, masks)
        loss = torch.mean(forward_score - gold_score)
        return loss

    def forward(self, sentence):  # dont confuse this with _forward_alg above.
        # Get the emission scores from the BiLSTM
        rnn_feats = self._get_rnn_features(sentence)
        # Find the best path, given the features.
        score, tag_seq = self._viterbi_decode(rnn_feats)
        return score, tag_seq
