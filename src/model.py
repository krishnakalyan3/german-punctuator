#!/usr/bin/env python3

import torch


class CharLSTMModel(torch.nn.Module):

    def __init__(self, input_size, hidden_size, output_size, n_layers=1):
        super(CharLSTMModel, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers
        self.embed = torch.nn.Embedding(input_size, hidden_size)
        self.rnn = torch.nn.LSTM(hidden_size, hidden_size, n_layers)
        self.h2o = torch.nn.Linear(hidden_size, output_size)

    def forward(self, input, hidden):
        embed = self.embed(input.view(1, -1))
        output, hidden = self.rnn(embed.view(1, 1, -1), hidden)
        output = self.h2o(output.view(1, -1))
        return output, hidden


if __name__ == '__main__':
    n_chars = len('abcd1234')
    model = CharLSTMModel(input_size=n_chars, hidden_size=15, output_size=n_chars)
    print(model)


# Embedding
# LSTM
# Linear

# Embedding
# LSTM
# Dense
