#!/usr/bin/env python3


def read_data(path):
    with open(path, 'r') as corpus:
        data = corpus.readlines()
    return data


class Dictionary(object):
    def __init__(self):
        self.word_id = {}
        self.id_word = []

    def add_word(self, word):
        if word not in self.word_id:
            self.word_id[word] = len(self.id_word) - 1
            self.id_word.append(word)
            return self.word_id[word]

    def __len__(self):
        return len(self.id_word)


if __name__ == '__main__':
    dict = Dictionary()
    print(dict)
