# Kama NMT Models

Here you can find information on chr2chr NMT models for Estonian-English and English-Estonian from the Kama project. The model files are too big for GitHub, so you can download them [here](http://statmt.ut.ee/kama).

The character-level approach we are following is the one by [Lee, Cho and Hofmann, 2016](https://arxiv.org/pdf/1409.0473v7.pdf), implemented in [DL4MT-c2c](https://github.com/nyu-dl/dl4mt-c2c). More specifically, we are training bilingual models (not multilingual) with characters (no BPE).

In the current experiments we used [Europarl](http://statmt.org/europarl) (17.1/12.8 mln En/Et tokens). Unlike the word-level NMT experiments, here there was no need to limit the vocabulary size.

The training time was about two weeks in most cases on a Tesla K40.

## Estonian-English Results

* BLEU: 32.5 ± 0.3
* METEOR: 34.5 ± 0.2
* TER: 49.2 ± 0.3

[Error analysis, examples]

## English-Estonian Results

* BLEU: 20.2 ± 0.3
* METEOR: 23.1 ± 0.2
* TER: 61.5 ± 0.3

[Error analysis, examples]
