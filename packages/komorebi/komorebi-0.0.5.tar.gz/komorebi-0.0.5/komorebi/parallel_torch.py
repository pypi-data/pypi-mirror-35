# -*- coding: utf-8 -*-

import torch
from torch import LongTensor
from torch.autograd import Variable

from komorebi.parallel import ParallelData


class TorchParallelData(ParallelData):
    def __init__(self, *args, **kwargs):
        super(TorchParallelData, self).__init__(*args, **kwargs)
        # PyTorch nonsense with CUDA... -_-|||
        if 'use_cuda' in kwargs:
            self.use_cuda = kwargs['use_cuda']
        else:
            self.use_cuda = torch.cuda.is_available()

    def create_variable(self, array_1d):
        """
        Create the PyTorch variable given a sentence

        :param array_1d: Input 1D array of vocab indices.
        :type array_1d: list(int)
        """
        result = Variable(LongTensor(array_1d).view(-1, 1))
        return result.cuda() if self.use_cuda else result

    def _iterate(self):
        """
        The helper function to iterate through the source and target file
        and convert the lines into vocabulary indices.
        """
        for src_line, trg_line in zip(self.src_data.lines(), self.trg_data.lines()):
            src_sent = self.create_variable(self.src_data.variable_from_sent(src_line, self.src_data.vocab))
            trg_sent = self.create_variable(self.trg_data.variable_from_sent(trg_line, self.trg_data.vocab))
            yield src_sent, trg_sent
