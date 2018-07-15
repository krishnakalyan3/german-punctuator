#!/usr/bin/env python3

import torch
from model import GruRNN

# Decide FEAT Vocoab
# Targat Vocab
# Check the dims


def main():
    input_chars = list(" \nabcdefghijklmnopqrstuvwxyz01234567890")
    output_chars = [".", ",", "?", ":", "n"]


def train():
    model.train()


if __name__ == '__main__':
    model = GruRNN(40, 2, 5)
