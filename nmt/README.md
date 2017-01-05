# Kama NMT Models

Here you can find information on word2word and chr2chr NMT models for Estonian-English and English-Estonian. The model files are too big for GitHub, so you can download them [here](http://statmt.ut.ee/kama).

## Neural word2word translation

The word-level approach we are following is the one by [Bahdanau et al, 2015](https://arxiv.org/pdf/1409.0473v7.pdf), implemented in [Nematus](https://github.com/rsennrich/nematus).

We apply BPE segmentation to both the input and the output, limiting the vocabulary to 40 000 entries. The acquired segmentation mostly corresponds to the linguistic intuition on frequent tokens (which are left intact) and medium-frequency tokens (which are split into compound parts or endings off stems); low-frequency tokens (also names, numeric tokens) are split into letters and letter pairs.

In the current experiments we used [Europarl](http://statmt.org/europarl) (17.1/12.8 mln En/Et tokens). The vocabulary size was set to 40 000 (also before experiments with BPE); this was the limit of what the GPU's memory could fit in.

The training time was about a week in most cases on a GTX 960 GPU.

## Estonian-English Results

* BLEU: 34.5 ± 0.3
* METEOR: 36.0 ± 0.2
* TER: 49.3 ± 0.4

The translations are either perfectly fluent (3 out of 4 translations), or include single errors/places that do not sound naturally. Long-distance dependencies modelled well (357, 952). The main problem is coverage: some times part of the input is skipped, and sometimes part of the translation output is unrelated to the input (1 in 4 translations). Small errors like wrong words are also present; this particularly affects names (like ``härra Gyürki'' translated as ``Mr Beaupuy'').

## English-Estonian Results

* BLEU: 23.1 ± 0.3
* METEOR: 25.1 ± 0.2
* TER: 60.4 ± 0.5

[Error analysis, examples]

## Neural chr2chr translation

[Bi-chr2chr. No vocabulary limit. Takes about 2 weeks to train (]

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
