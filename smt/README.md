# Kama SMT Models

Here you can find information on the Estonian-English and English-Estonian statistical MT models developed in the Kama project, as well as the translation output of the models applied to several test sets (under the [corpora](http://github.com/fishel/kama/tree/master/corpora) folder. The model files are too big for GitHub, so you can download them [here](http://statmt.ut.ee/kama).

## Description

The models represented here are statistical phrase-based translation models. In parallel we are testing the various neural MT approaches, but for now the most usable baseline in terms of industrial collaborations is statistical.

We are using [Moses](http://statmt.org/moses). Six different corpora are used for training

[Data, sizes, TMCombine/interpolate-lm]

## Estonian-English Results

* BLEU: 32.4 ± 0.3
* METEOR 35.8 ± 0.1
* TER 51.3 ± 0.3

Largely the translation output conveys the meaning correctly, but lacks in fluency. This ranges from understandable phrases connected with wrong functional words to word salad translations. Some sentences, especially short ones, get near-perfect translations. Once in a while an important word is missing, but overall coverage of the input text is ok.

### Examples

|    |     |
| ------------ | ---------- |
| **Source:**         |    tarbijakaitse roheline raamat ei tõstatanud küll kõiki neid küsimusi , kuid neid käsitletakse selles raportis . |
| **Hypothesis:**     |    the Green Paper on consumer protection not raised right all these issues , but they are covered in this report . |
| **Reference:**      |    not all these matters were raised in the Green paper on consumer protection but they are in this report . |
**Analysis:** fluency limping, word order closely follows the input.

|    |     |
| ------------ | ---------- |
| **Source:**         |    nagu ma ütlesin , olles kokku leppinud ühisstrateegias , kindlas tegevuskavas ning konkreetsetes jätkumehhanismides , arutanud selliseid tähtsaid ja päevakajalisi küsimusi nagu kliimamuutused , integratsioon , energia ja sisseränne , kujutab tippkohtumine selgelt sammu edasi , meie Aafrikaga suhte küpsemist . |
| **Hypothesis:**     |    as I said , having agreed on a joint strategy , a specific action plan , and the specific jätkumehhanismides discussed , such important and topical issues such as climate change , energy and immigration , integration , clearly the Summit represents a step forward in our relationship with Africa maturation . |
| **Reference:**      |    as I have said , by agreeing a joint strategy , a specific action plan and concrete follow-up mechanisms , by discussing such important and current issues as climate change , integration , energy and immigration , the summit clearly represents a step forward , a maturing of our relationship with Africa . |
**Analysis:** fluency heavily limping, repetition (such ... such), an OOV compound

|    |    |
| ----- | ----- |
| **Source:** |              seda gaasi leidub suures koguses Prantsusmaal , Poolas ja Bulgaarias . |
| **Hypothesis:** |        this gas there are large quantities of France , Poland and Bulgaria . |
| **Reference:** |           large amounts of this gas are found in France , Poland and Bulgaria . |
**Analysis:** fluency again, this time the errors changing the meaning

## English-Estonian Results

* BLEU: 19.3 ± 0.3
* 23.2 ± 0.2
* 60.3 ± 0.3

Again, the meaning of the translation in most cases coincides with the meaning of the input sentence. Due to richer morphology of Estonian, the fluency problems are much more evident. The output is mostly a direct translation of the input, with practically no reordering. This affects long-distance reordering (like "between A, B and C" - "A, B ja C vahel"), which mostly fails to get translated correctly.

### Examples

|    |    |
| ----- | ----- |
| **Source:** |              some are Greeks , who are treated differently from other Europeans . |
| **Hypothesis:** |        mõned on kreeklased , kes koheldakse erinevalt teistest eurooplased . |
| **Reference:** |           mõned on kreeklased , keda koheldakse teistest eurooplastest erinevalt . |
**Analysis:**  one minor inflection mistake (kes/keda) and English word order preserved

|    |    |
| ----- | ----- |
| **Source:** |              but , thanks to the good cooperation between Parliament and the Commission and the Member States , at the end we have got that agreement . |
| **Hypothesis:** |        kuid tänu hea koostöö parlamendi ja komisjoni vahel ja liikmesriikides , on meil lõpuks on see kokkulepe . |
| **Reference:** |           kuid tänu heale koostööle parlamendi , komisjoni ja liikmesriikide vahel on lõpuks kokkuleppele jõutud . |
**Analysis:** no agreement in terms of morphology, repetition "on .. on", failed to place "vahel/between" on the right spot, English word order mostly preserved

|    |    |
| ----- | ----- |
| **Source:** |              however many fences we put up , whatever efforts we make , we need a global strategy and solidarity between the European states .
| **Hypothesis:** |        kuid paljud aiad me panema , olenemata jõupingutusi teeme , siis vajame ülemaailmset strateegiat ja solidaarsuse Euroopa riikides .
| **Reference:** |           ei ole oluline , kui palju tõkkeid ehitame või milliseid meetmeid võtame , Euroopa riikide vahel on vaja üleüldist strateegiat ja solidaarsust .
**Analysis:** direct translation with bad fluency, practically impossible to understand
