#!/usr/bin/env bash

wget -q -P data/ https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/comtrans.zip
unzip data/comtrans.zip -d data/

mkdir -p data/pre_proc/en
mkdir -p data/pre_proc/de
