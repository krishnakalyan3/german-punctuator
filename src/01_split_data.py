#!/usr/bin/env python3
import os
from utils import read_data
EN_DATA = '../data/comtrans_en.txt'
DE_DATA = '../data/comtrans_de.txt'
OUT_PATH = '../data/pre_proc'


def split_data(type, data):
    dest_train = os.path.join(OUT_PATH, type, 'train.txt')
    dest_valid = os.path.join(OUT_PATH, type, 'valid.txt')
    dest_test = os.path.join(OUT_PATH, type, 'test.txt')

    # Write Data
    with open(dest_train, 'w') as f_train, open(dest_valid, 'w') as f_valid, open(dest_test, 'w') as f_test:
        for i, v in enumerate(data):

            if i % 10 == 0:
                f_valid.write(v)
            elif i % 10 == 1:
                f_test.write(v)
            elif i % 10 > 2:
                f_train.write(v)


if __name__ == '__main__':
    data_en = read_data(EN_DATA)
    split_data('en', data_en)

    data_de = read_data(DE_DATA)
    split_data('de', data_de)
