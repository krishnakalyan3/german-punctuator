#!/usr/bin/env python3

import torch
import argparse
from model import CharLSTMModel
from utils import read_data

# Decide FEAT Vocoab
# Targat Vocab
# Check the dims

def train(epochs):
    pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PyTorch CharLSTM Example')
    parser.add_argument('--cuda', action='store_true',
                        help='use cuda')
    parser.add_argument('--batch_size', type=int, default=4)
    parser.add_argument('--learning_rate', type=float, default=0.01)
    args = parser.parse_args()

    device = torch.device("cuda" if args.cuda else "cpu")
    # read_data

    n_chars = 10
    model = CharLSTMModel(input_size=n_chars, hidden_size=15, output_size=n_chars)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.learning_rate)
