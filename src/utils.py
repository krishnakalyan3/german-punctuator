#!/usr/bin/env python3


def read_data(path):
    with open(path, 'r') as corpus:
        data = corpus.readlines()
    return data
