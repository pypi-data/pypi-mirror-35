# -*- coding: utf-8 -*-
"""Utils tools for tagger
Created by InfinityFuture
"""

from collections import Counter
import numpy as np
import torch
from sklearn.utils import shuffle

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
    return torch.tensor(idxs, dtype=torch.long) # pylint: disable=not-callable

def default_spliter(seq):
    """Default sentence spliter"""
    if isinstance(seq, list):
        return seq
    if isinstance(seq, str):
        return seq.split()
    raise Exception('invalid type(seq) for default_spliter')

def text_reader(path, spliter=default_spliter):
    """Read a text file, and return data
    data should follow this format:

    I want to New York

    O O O B-City I-City

    """
    with open(path, 'r') as fobj:
        lines = []
        for line in fobj:
            line = line.strip()
            if line:
                lines.append(line)
    assert lines, 'text file empty "{}"'.format(path)
    assert len(lines) % 2 == 0, 'text file should have even lines "{}"'.format(path)

    x_data = []
    y_data = []
    for i, tag in enumerate(lines):
        if i % 2 == 1:
            line = lines[i - 1]
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
        indx = len(word_to_ix)
        word_to_ix[word] = indx

    ix_to_word = {
        v: k
        for k, v in word_to_ix.items()
    }

    tag_to_ix = {
        PAD_TAG: 0,
        UNK_TAG: 1,
        START_TAG: 2,
        STOP_TAG: 3
    }

    for tag in tags_word.keys():
        indx = len(tag_to_ix)
        tag_to_ix[tag] = indx

    ix_to_tag = {
        v: k
        for k, v in tag_to_ix.items()
    }

    return {
        'word_to_ix': word_to_ix,
        'ix_to_word': ix_to_word,
        'tag_to_ix': tag_to_ix,
        'ix_to_tag': ix_to_tag,
    }

def pad_seq(seq: list, max_len: int) -> list:
    """Padding data to max_len length"""
    if len(seq) < max_len:
        return seq + [PAD_TAG] * (max_len - len(seq))
    return seq

def batch_flow(x_data: list, y_data: list, # pylint: disable=too-many-arguments
               word_to_ix: dict, tag_to_ix: dict,
               batch_size: int = 32, sample_shuffle=True):
    """Automatic generate batch data"""
    assert len(x_data) >= batch_size, 'len(x_data) > batch_size'
    assert len(x_data) == len(y_data), \
        'len(x_data) == len(y_data), {} != {}'.format(len(x_data), len(y_data))
    if sample_shuffle:
        x_data, y_data = shuffle(x_data, y_data)

    x_batch, y_batch, len_batch = [], [], []
    ind = 0
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

            len_batch = [
                torch.tensor(t, dtype=torch.long) # pylint: disable=not-callable
                for t in len_batch
            ]

            tcx, tcy, tcl = torch.stack(x_batch), torch.stack(y_batch), torch.stack(len_batch)
            x_batch, y_batch, len_batch = [], [], []
            yield tcx, tcy, tcl

        x_batch.append(x_data[ind])
        y_batch.append(y_data[ind])
        len_batch.append(len(y_data[ind]))

        ind += 1
        if ind >= len(x_data):
            ind = 0

def sequence_mask(lens: torch.Tensor, max_len: int = None) -> torch.FloatTensor:
    """InfinityFutures: This function is copy from:

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
    for i, tag in enumerate(seq):
        if tag.startswith('B') or tag.startswith('O'):
            if start_ind >= 0:
                ret.append((start_ind, i, start_type))
                start_ind, start_type = -1, None
        if tag.startswith('B'):
            start_ind = i
            start_type = tag[1:]
    if start_ind >= 0:
        ret.append((start_ind, len(seq), start_type))
        start_ind, start_type = -1, None
    return ret
