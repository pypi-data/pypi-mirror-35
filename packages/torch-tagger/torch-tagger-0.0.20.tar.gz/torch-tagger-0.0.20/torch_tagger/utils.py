# -*- coding: utf-8 -*-
# From https://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html
# Modified by InfinityFuture

from collections import Counter
import numpy as np
import torch

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
START_TAG = '<START>'
STOP_TAG = '<STOP>'
PAD_TAG = '<PAD>'
UNK_TAG = '<UNK>'

def prepare_sequence(seq, to_ix) -> torch.LongTensor:
    """Convert sequence to torch variable"""
    idxs = [
        to_ix[w] if w in to_ix else to_ix[UNK_TAG]
        for w in seq
    ]
    return torch.tensor(idxs, dtype=torch.long)

def default_spliter(x) -> list:
    """Default sentence spliter"""
    return x.split()

def text_reader(path, spliter=default_spliter):
    """Read a text file, and return data
    data should follow this format:
    I want to New York
    O O O CityB CityI
    """
    with open(path, 'r') as fp:
        lines = []
        for l in fp:
            l = l.strip()
            if len(l):
                lines.append(l)
    assert len(lines) > 0, 'text file empty "{}"'.format(path)
    assert len(lines) % 2 == 0, 'text file should have even lines "{}"'.format(path)
    x_data = []
    y_data = []
    for i, l in enumerate(lines):
        if i % 2 == 1:
            line = lines[i - 1]
            tag = l
            line = spliter(line)
            tag = spliter(tag)
            x_data.append(line)
            y_data.append(tag)
            assert len(line) == len(tag), 'line "{}" and "{}" do not match'.format(i - 1, i)
    return x_data, y_data

def build_vocabulary(x_data: list, y_data: list) -> dict:
    """ Use data to build vocabulary"""
    sentence_word = Counter()
    tags_word = Counter()
    for sentence in x_data:
        sentence_word.update(sentence)
    for tags in y_data:
        tags_word.update(tags)

    word_to_ix = {
        PAD_TAG: 0,
        UNK_TAG: 1
    }
    for word in sentence_word.keys():
        ix = len(word_to_ix)
        word_to_ix[word] = ix
    
    ix_to_word = {v: k for k, v in word_to_ix.items()}

    tag_to_ix = {
        PAD_TAG: 0,
        UNK_TAG: 1,
        START_TAG: 2,
        STOP_TAG: 3
    }

    for tag in tags_word.keys():
        ix = len(tag_to_ix)
        tag_to_ix[tag] = ix

    ix_to_tag = { v: k for k, v in tag_to_ix.items()}

    return {
        'word_to_ix': word_to_ix,
        'ix_to_word': ix_to_word,
        'tag_to_ix': tag_to_ix,
        'ix_to_tag': ix_to_tag,
    }

def pad_seq(x: list, max_len: int) -> list:
    """Padding data to max_len length"""
    if len(x) < max_len:
        return x + [PAD_TAG] * (max_len - len(x))
    return x

def batch_flow(x_data: list, y_data: list, word_to_ix: dict, tag_to_ix: dict, batch_size: int= 32):
    """Automatic generate batch data"""
    assert len(x_data) > 0, 'len(x_data) > 0'
    assert len(x_data) == len(y_data), 'len(x_data) == len(y_data), {} != {}'.format(len(x_data), len(y_data))

    x_batch, y_batch, len_batch = [], [], []
    while True:
        if len(x_batch) == batch_size:
            max_len = np.max([len(t) for t in x_batch])
            x_batch = [pad_seq(x, max_len) for x in x_batch]
            y_batch = [pad_seq(y, max_len) for y in y_batch]
            x_batch = [prepare_sequence(x, word_to_ix) for x in x_batch]
            y_batch = [prepare_sequence(y, tag_to_ix) for y in y_batch]

            batches = list(zip(x_batch, y_batch, len_batch))
            batches = sorted(batches, key=lambda x: x[2], reverse=True)
            x_batch = [t[0] for t in batches]
            y_batch = [t[1] for t in batches]
            len_batch = [t[2] for t in batches]

            len_batch = [torch.tensor(t, dtype=torch.long) for t in len_batch]

            tx, ty, tl = torch.stack(x_batch), torch.stack(y_batch), torch.stack(len_batch)
            x_batch, y_batch, len_batch = [], [], []
            yield tx, ty, tl

        ind = np.random.randint(0, len(x_data))
        x = x_data[ind]
        y = y_data[ind]

        x_batch.append(x)
        y_batch.append(y)
        len_batch.append(len(x))

def sequence_mask(lens: torch.Tensor, max_len: int = None) -> torch.FloatTensor:
    """InfinityFutures:
    This function is copy from:
    https://github.com/epwalsh/pytorch-crf
    The author is epwalsh, and its license is MIT too

    Compute sequence mask.
    Parameters
    ----------
    lens : torch.Tensor
        Tensor of sequence lengths ``[batch_size]``.
    max_len : int, optional (default: None)
        The maximum length (optional).
    Returns
    -------
    torch.ByteTensor
        Returns a tensor of 1's and 0's of size ``[batch_size x max_len]``.
    """
    batch_size = lens.size(0)

    if max_len is None:
        max_len = lens.max().item()

    ranges = torch.arange(0, max_len, device=lens.device).long()
    ranges = ranges.unsqueeze(0).expand(batch_size, max_len)
    ranges = torch.autograd.Variable(ranges)

    lens_exp = lens.unsqueeze(1).expand_as(ranges)
    mask = ranges < lens_exp

    return mask.float()

def extrat_entities(seq: list) -> list:
    """Extract entities from a sequences
    ---
    input: ['B', 'I', 'I', 'O', 'B', 'I']
    output: [(0, 3, ''), (4, 6, '')]
    ---
    input: ['B-loc', 'I-loc', 'I-loc', 'O', 'B-per', 'I-per']
    output: [(0, 3, '-loc'), (4, 6, '-per')]
    """
    ret = []
    start_ind, start_type = -1, None
    for i, s in enumerate(seq):
        if s.startswith('B') or s.startswith('O'):
            if start_ind >= 0:
                ret.append((start_ind, i, start_type))
                start_ind, start_type = -1, None
        if s.startswith('B'):
            start_ind = i
            start_type = s[1:]
    if start_ind >= 0:
        ret.append((start_ind, len(seq), start_type))
        start_ind, start_type = -1, None
    return ret
