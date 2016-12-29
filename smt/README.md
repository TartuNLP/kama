# Kama SMT Models

Here you can find information on the Estonian-English and English-Estonian statistical MT models developed in the Kama project, as well as the translation output of the models applied to several test sets (under the [corpora](http://github.com/fishel/kama/tree/master/corpora) folder. The model files are too big for GitHub, so you can download them [here](http://statmt.ut.ee/kama).

## Description

The models represented here are statistical phrase-based translation models. Yes, there is NMT now -- we are experimenting with it, etc.

[PBSMT, Moses]. [NMT still experimented with, online service running on PBSMT].

[Data, sizes, TMCombine/interpolate-lm]

## Estonian-English Results

* BLEU: 32.4 ± 0.3
* METEOR 35.8 ± 0.1
* TER 51.3 ± 0.3

The main observation is that the output is often disfluent. This ranges from understandable phrases connected with wrong functional words to word salad translations. Some sentences, especially short ones, get near-perfect translations. Once in a while an important word is missing, but overall coverage of the input text is ok. Examples:

| **Source:**         |    tarbijakaitse roheline raamat ei tõstatanud küll kõiki neid küsimusi , kuid neid käsitletakse selles raportis .
| **Reference:**      |    not all these matters were raised in the Green paper on consumer protection but they are in this report .
| **Hypothesis:**     |    the Green Paper on consumer protection not raised right all these issues , but they are covered in this report .
| **Analysis:**       |    fluency limping, word order closely follows the input

| **Source:**         |    nagu ma ütlesin , olles kokku leppinud ühisstrateegias , kindlas tegevuskavas ning konkreetsetes jätkumehhanismides , arutanud selliseid tähtsaid ja päevakajalisi küsimusi nagu kliimamuutused , integratsioon , energia ja sisseränne , kujutab tippkohtumine selgelt sammu edasi , meie Aafrikaga suhte küpsemist .
| **Reference:**      |    as I have said , by agreeing a joint strategy , a specific action plan and concrete follow-up mechanisms , by discussing such important and current issues as climate change , integration , energy and immigration , the summit clearly represents a step forward , a maturing of our relationship with Africa .
| **Hypothesis:**     |    as I said , having agreed on a joint strategy , a specific action plan , and the specific jätkumehhanismides discussed , such important and topical issues such as climate change , energy and immigration , integration , clearly the Summit represents a step forward in our relationship with Africa maturation .
| **Analysis:**       |    fluency heavily limping, repetition (such ... such), an OOV compound

## English-Estonian Results
