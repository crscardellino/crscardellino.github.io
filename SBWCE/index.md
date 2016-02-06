---
layout: default
---

Summary
-------

This is the Spanish Billion Words Corpus and Embeddings linguistic resource.

This resource consists of an unannotated corpus of the Spanish language of
nearly 1.5 billion words, compiled from different corpora and resources from the
web; and a set of word vectors (or embeddings), created from this corpus using
the [word2vec algorithm](https://code.google.com/p/word2vec/), provided by the
[gensim package](https://radimrehurek.com/gensim/). These embeddings were
evaluated with a
[translation](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/questions-words_sp.txt)
of [word2vec's question
words](https://code.google.com/p/word2vec/source/browse/trunk/questions-words.txt).

The cleaned corpus is publicly available to download as [raw text
file](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/clean_corpus.tar.bz2). The
word vectors are also available to download in [word2vec's binary
format](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz)
and in [text
format](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.txt.bz2).

### Disclaimer

I tried to find all the Spanish corpora, from different sources, that were
available to download freely from the web. No copyright infringement was
intended and I also tried to acknowledge correctly all the original authors of
the corpora I borrowed.

If you are an author of one of the resources and feel your work wasn't correctly
used in this resource please feel free to [contact
me](mailto:ccardellino@famaf.unc.edu.ar) and I will remove your work from this
corpus and from the embeddings.

Likewise, if you are author or know of some other resources publicly available
for the Spanish language (the corpus doesn't need to be annotated) and want to
contribute, also feel free to [contact me](mailto:ccardellino@famaf.unc.edu.ar).

Corpora
-------

The corpus was created compiling the following resources of the Spanish
language (the resources were found publicly available on the internet):

* Spanish portion of [SenSem](http://grial.uab.es/fproj.php?id=10&idioma=in).
* Spanish portion of the [Ancora Corpus](http://clic.ub.edu/corpus/en).
* [Tibidabo Treebank and IULA Spanish LSP
  Treebank](http://lod.iula.upf.edu/resources/metadata_TRL_Tibidabo_LSP_treebank_ES).
* The Spanish portion of the following [OPUS
  Project](http://opus.lingfil.uu.se/index.php) Corpora:
    * The [books](http://opus.lingfil.uu.se/Books.php) aligned by [Andras
      Farkas](http://www.farkastranslations.com/).
    * The [JRC-Acquis](http://opus.lingfil.uu.se/JRC-Acquis.php) collection of
      legislative text of the European Union.
    * The [News Commentary](http://opus.lingfil.uu.se/News-Commentary.php)
      corpus.
    * The [United Nations](http://opus.lingfil.uu.se/UN.php) documents compiled
      by Alexandre Rafalovitch and Robert Dale.
* The Spanish portion of the [Europarl](http://statmt.org/europarl/) (European
  Parliament), compiled by Philipp Koehn.
* Dumps from the Spanish [Wikipedia](https://es.wikipedia.org),
  [Wikisource](https://es.wikisource.org) and
  [Wikibooks](https://es.wikibooks.org) on date 2015-09-01, parsed with the
  [Wikipedia Extractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor).

Corpus Processing
-----------------

All the annotated corpora (like Ancora, SenSem and Tibidabo) were untagged,
since word2vec works with unannotated data.  The parallel corpora (most coming
from the OPUS Project) was preprocessed to obtain only the Spanish portions of
it.

Once we had the whole corpus unannotated, we proceed to replace all
non-alphanumeric characters with whitespaces. All numbers with the token
"DIGITO" and all the multiple whitespaces with only one whitespace.

The capitalization of the words remain unchanged.

Parameters for Embeddings Training
----------------------------------

To train the word embeddings we used the following parameters:

* The selected algorithm was the _skip-gram_ model with _negative-sampling_.
* The minumum word frequency was 5.
* The amount of "noise words" for the negative sampling was 20.
* The 273 most common words were downsampled.
* The dimension of the final word embedding was 300.

Description of Resulting Embeddings
-----------------------------------

The original corpus had the following amount of data:

* A total of 1420665810 raw words.
* A total of 46925295 sentences.
* A total of 3817833 unique tokens.

After the skip-gram model was applied, filtering of words with less than 5
occurrences as well as the downsample of the 273 most common words, the
following values were obtained:

* A total of 771508817 raw words.
* A total of 1000653 unique tokens.

The final resource was a corpus of 1000653 word embeddings of dimension 300.

Evaluation of the Embeddings
----------------------------

This corpus was evaluated using a translation of the original word2vec's
question words. The accuracy results are the following:

* Capital of common countries: 0.84
* Capitals of the World: 0.68
* City in state: 0.27
* Currency: 0.08
* Family: 0.80
* Adjective to adverbs: 0.21
* Opposite: 0.24
* Present participle: 0.73
* Nationality adjective: 0.28
* Past tense: 0.25
* Plural: 0.51
* Plural verbs: 0.42

License
-------

<div style="text-align: center;">
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
<span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Spanish Billion Word
Corpus and Embeddings</span>
by <span xmlns:cc="http://creativecommons.org/ns#"
property="cc:attributionName">Cristian Cardellino</span><br />
is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
</div>
