#!/usr/bin/env python3

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# Implement mini-batch
class GruRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, batch_size=1, layers=1, bi=False):
        """
        IMPORTANT: Use batch_first convention for ease of use.
                   However, the hidden layer still use batch middle convension.
        """
        super(GruRNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.batch_size = batch_size
        self.layers = layers
        self.bi_mul = 2 if bi else 1

        self.encoder = nn.Linear(input_size, hidden_size)
        self.gru = nn.GRU(input_size, hidden_size, self.layers, bidirectional=bi, batch_first=True)
        self.decoder = nn.Linear(hidden_size * self.bi_mul, output_size)
        self.softmax = F.softmax

    def forward(self, x, hidden):
        embeded = x
        gru_output, hidden = self.gru(embeded, hidden.view(self.layers * self.bi_mul, -1, self.hidden_size))
        gru_output.contiguous()
        output = self.decoder(gru_output.view(-1, self.hidden_size * self.bi_mul))
        return output.view(self.batch_size, -1, self.output_size), hidden

    def init_hidden(self, random=False):
        if random:
            return Variable(torch.randn(self.layers * self.bi_mul, self.batch_size, self.hidden_size))
        else:
            return Variable(torch.zeros(self.layers * self.bi_mul, self.batch_size, self.hidden_size))


class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleModel, self).__init__()

        self.encoder = nn.Embedding(input_size, hidden_size)


    pass



# Embedding
# Dense

# Embedding
# LSTM
# Dense

# Convo 1D
# Dense