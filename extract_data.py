#!/usr/bin/env python3

with open('data/comtrans/alignment-de-en.txt', 'r', encoding='utf-8', errors='ignore') as f_in, \
        open('data/comtrans_en.txt', 'w') as f_out_en, \
        open('data/comtrans_de.txt', 'w') as f_out_de:
    num_lines = 0
    for l in f_in.readlines():
        if num_lines == 0:
            f_out_de.write(l)
        if num_lines == 1:
            f_out_en.write(l)

        num_lines = (0 if num_lines == 2 else num_lines + 1)
