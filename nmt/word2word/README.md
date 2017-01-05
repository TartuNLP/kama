# Kama NMT Models

Here you can find information on word2word NMT models for Estonian-English and English-Estonian from the Kama project. The model files are too big for GitHub, so you can download them [here](http://statmt.ut.ee/kama).

The approach we followed in these experiments is the one by [Bahdanau et al, 2015](https://arxiv.org/pdf/1409.0473v7.pdf), implemented in [Nematus](https://github.com/rsennrich/nematus).

We apply BPE segmentation to both the input and the output, limiting the vocabulary to 40 000 entries. The acquired segmentation mostly corresponds to the linguistic intuition on frequent tokens (which are left intact) and medium-frequency tokens (which are split into compound parts or endings off stems); low-frequency tokens (also names, numeric tokens) are split into letters and letter pairs.

In the current experiments we used [Europarl](http://statmt.org/europarl) (17.1/12.8 mln En/Et tokens). The vocabulary size was set to 40 000 (also before experiments with BPE); this was the limit of what the GPU's memory could fit in.

The training time was about a week in most cases on a GTX 960 GPU.

## Estonian-English Results

* BLEU: 34.5 ± 0.3
* METEOR: 36.0 ± 0.2
* TER: 49.3 ± 0.4

The translations are either perfectly fluent (3 out of 4 translations), or include single errors/places that do not sound naturally. Long-distance dependencies modelled well. The main problem is coverage: some times part of the input is skipped, and sometimes part of the translation output is unrelated to the input (1 in 4 translations). Small errors like wrong words are also present; this particularly affects names (like "härra Gyürki" translated as "Mr Beaupuy").

|    |     |
| ------------ | ---------- |
|**Source:** |                 eriti tervitan ma , hr Barroso , teist põhimõtet : õiglus ja liikmesriikide erinevate lähtekohtade ja investeerimisvõimaluste tunnistamine . |
|**Hypothesis (NMT):** |                  I particularly welcome , Mr Barroso , your principle : fairness and the recognition of different starting points and investment opportunities for Member States . |
|**Hypothesis (SMT)**: |                  I particularly welcome , Mr Barroso , the second principle : justice and of the Member States of the different points of departure and the recognition of investment opportunities . |
|**Reference:** |                 in particular , Mr Barroso , I welcome the second principle : fairness and recognising Member States' different starting points and different capacities to invest . |
**Analysis:** near-perfect translation by NMT, perfect fluency, including a long-distance reordering ("liikmesriikide X ja Y" - "X and Y for Member States"). One mistake: "teist" wrongly translated as "your" (should have been "second")


|    |     |
| ------------ | ---------- |
|**Source:** |                 kirjalikult . - ( IT ) Austatud juhataja , daamid ja härrad . mina hääletasin härra Gyürki riiklikke energiasäästu tegevuskavasid järelkajastava raporti poolt .|
|**Hypothesis (NMT):** |                 in writing . - ( IT ) Madam President , ladies and gentlemen , I voted in favour of Mr Beaupuy 's report on the national energy saving action plans .|
|**Hypothesis (SMT):** |                 in writing . - ( IT ) Mr President , ladies and gentlemen . I voted against Mr Gyürk 's national energy efficiency action plans järelkajastava in favour of the report .|
|**Reference:** |                 in writing . - ( IT ) Madam President , ladies and gentlemen , I voted in favour of Mr Gyürk 's report on follow-up of the energy efficiency national action plans .|
**Analysis:** good translation with perfect fluency, but minor adequacy problems: guessing the "Madam" President from the genderless Estonian input wrongly, the name "Gyürk" is translated as "Beaupuy" (segmented with BPE as ``Gy@@ ür@@ ki``; only present in the training set 3 times in the genitive form). Impressive, that "hääletasin ... poolt" is correctly translated by NMT as "voted in favor of", unlike SMT's erroneous guess "voted against".

## English-Estonian Results

* BLEU: 23.1 ± 0.3
* METEOR: 25.1 ± 0.2
* TER: 60.4 ± 0.5
