# Kama

This repository holds the scripts, models and descriptions for the output of research of neural machine translation at TartuNLP. A live demo of the latest models is available at [translate.ut.ee](https://translate.ut.ee). Below you will find a brief description of the latest approach, links to trained MT models and source code for running the models as an MT server and an API service.

## Why "Kama"?
Our first MT project was called "KaMa: **ka**sutatav eesti **ma**sintõlge" (Usable Estonian Machine Translation). [Kama](https://en.wikipedia.org/wiki/Kama_(food)) is also a national Estonian food item :-)

# Description

Our current approach is multilingual multi-domain neural machine translation. That means that a single NMT model translates between several languages and is also aware of the text domain of the texts it works with.

More specifically, we use the [Transformer](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) with the output language and text domain as additional input information. The approach is described in [this paper](https://www.aclweb.org/anthology/W19-5342.pdf).

Besides multilingual translation, the approach exhibits interesting additional functionality, such as handling code-switching and monolingual zero-shot translation, that can be used for error correction and style adaptation.

## Code switching

## Error correction

## Style adaptation

# Software

# Models

# Projects

The work has been part of several projects and collaborations. National projects:
* KaMa: kasutatav eesti masintõlge (Usable Estonian Machine Translation), 2015--2017, funded by [NPELT](http://keeletehnoloogia.ee)
* Neurotõlge: Adaptive, Multilingual and Reliable Machine Translation for Estonian, 2018--2020, funded by [NPELT](http://keeletehnoloogia.ee)

Related projects:
* [Bergamot](https://browser.mt/), Horizon 2020 Research and Innovation Action, grant agreement No 825303
