# Kama

This repository holds the scripts, models and descriptions for the output of research of neural machine translation at TartuNLP. A live demo of the latest models is available at [translate.ut.ee](https://translate.ut.ee). Below you will find a brief description of the latest approach, links to trained MT models and source code for running the models as an MT server and an API service.

## Why "Kama"?
Our first MT project was called "KaMa: **ka**sutatav eesti **ma**sintõlge" (Usable Estonian Machine Translation). [Kama](https://en.wikipedia.org/wiki/Kama_(food)) is also a national Estonian food item :-)

# Description

Our current approach is multilingual multi-domain neural machine translation. That means that a single NMT model translates between several languages and is also aware of the text domain of the texts it works with.

More specifically, we use the [Transformer](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) with the output language and text domain as additional input information. The approach is described in [this paper](https://www.aclweb.org/anthology/W19-5342.pdf).

Besides multilingual translation, the approach exhibits interesting additional functionality, such as handling code-switching and monolingual zero-shot translation, that can be used for error correction and style adaptation. Some examples from our current 7-language model:

## Code switching examples

* Sie können kirjutada daudz gemischt языки, and see переведёт kõik into vienu keelde. -> You can write a lot of mixed languages, and it translates everything into one language.
* Sie können kirjutada daudz gemischt языки, and see переведёт kõik into vienu keelde. -> Te võite kirjutada palju sega keeli, ja see tõlgib kõik ühte keelde.
* Sie können kirjutada daudz gemischt языки, and see переведёт kõik into vienu keelde. -> Вы можете написать много смешанных языков, и это переводит все в одно язык.

## Error correction examples

* Ich legen Buch an Regal neben Tisch. -> Ich lege das Buch an Regal neben dem Tisch.
* Ma arvab et homme miski põnev näeb. -> Ma arvan, et homme näeb midagi põnevat.
* Наш программа переводит текст с ошибок в правильную. -> Наша программа переводит текст с ошибками в правильный.

English correction does not work all too well, with some rare examples:
* I be large reader, I has big library. -> I am a big reader, I have a big library.

## Style adaptation examples

Cross-lingual:
* That is freaky -> See on kohutav. (formal) / See on vastik. (informal)
* That is freaky -> Это ужасно. (formal) / Это отвратительно. (informal)

Monolingual:
* Kes oled? -> Kes te olete? (formal)
* Wer bist du? -> Wer sind Sie? (formal)
* I will be remunerated. -> I'll be rewarded. (informal)

# Models

All our models are currently trained with [Sockeye](https://github.com/awslabs/sockeye) using [open parallel corpora](http://opus.nlpl.eu/), pre-processed with our [truecaser](https://github.com/tartunlp/truecaser) and Google's [SentencePiece](https://github.com/google/sentencepiece).

Models with their language and domain combinations:

* English-German-French, Europarl-OpenSubtitles-JRCAcquis
  * [Sockeye version 1.18.56]()

* English-Estonian-Latvian, Europarl-OpenSubtitles-JRCAcquis-EMEA
  * [Sockeye version 1.18.56]()

* English-Estonian-Latvian-Russian, Europarl-OpenSubtitles-JRCAcquis-EMEA-UNcorpus-DGTTM-ParaCrawl-NewsCommentary
  * [Sockeye version 1.18.56]()

* English-Estonian-Latvian-Lithuanian-Russian-German-Finnish, Europarl-OpenSubtitles-JRCAcquis-EMEA-DGTTM-ParaCrawl-NewsCommentary
  * [Sockeye version 1.18.106]()

# Software

NMT provider implementation: [Nazgul](https://github.com/TartuNLP/nazgul)

NMT API server implementation: [Sauron](https://github.com/TartuNLP/sauron)

# Projects

The work has been part of several projects and collaborations. National projects:
* KaMa: kasutatav eesti masintõlge (Usable Estonian Machine Translation), 2015--2017, funded by [NPELT](http://keeletehnoloogia.ee)
* Neurotõlge: Adaptive, Multilingual and Reliable Machine Translation for Estonian, 2018--2020, funded by [NPELT](http://keeletehnoloogia.ee)

Related projects:
* [Bergamot](https://browser.mt/), Horizon 2020 Research and Innovation Action, grant agreement No 825303
