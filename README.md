# Kama

Kama: Usable Estonian Machine Translation (kasutatav masintõlge) is a project (2015-2017) under the [National Programme for Estonian Language Technology](http://keeletehnoloogia.ee). Its focus is improving machine translation from/into Estonian and making sure that its output is usable in practice for specific text domains, for example for post-editing.

Here we publicly distribute the latest SMT and NMT models that we have developed, as well as their analysis and test set translations.

## NMT

We are working on [word2word](https://arxiv.org/abs/1409.0473) and [chr2chr](https://arxiv.org/abs/1610.03017) neural MT approaches. You can find the model files, translation quality estimations and references to used software in the [nmt](http://github.com/fishel/kama/tree/master/nmt) folder.

## SMT

Our previous baseline was phrase-based SMT, and included a number of improvements on top of the baseline approach. In the [smt](http://github.com/fishel/kama/tree/master/smt) folder you will find the models, analysis of translation quality and other info.
