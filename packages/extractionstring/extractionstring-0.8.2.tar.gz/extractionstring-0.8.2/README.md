# Tokenization for language processing

This package contains some generic configurable tools allowing to cut a string in sub-parts (cf. [Wikipedia](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization)), called `ExtractionString`. An `ExtractionString` is a sub-string from a parent string (say the initial complete text), with associated intervals of non-overlaping characters. The number of associated intervals is arbitrary. 

`ExtractionString` class allow basic tokenization of text, such as word splitting, n-gram splitting, char-gram splitting of arbitrary size. In addition, it allows to associate several non-overlapping sub-strings into a given `ExtractionString`. One can compare two different `ExtractionString` objects in terms of their intervals. One can also apply basic mathematical operations and logic to them (+, -, *, /) corresponding to the union, difference, intersection and symmetric difference implemented by Python set ; here the sets are the intervals of position from the parent string. Finally, there are some ordering possibilities among the different `ExtractionString` constructed from the same parent string.

## Depositories, and online documentation

The different sources of informations for this packages are : 
 
 - the official Python Package Installation (PyPI) repository is on [https://pypi.org/project/extractionstring](https://pypi.org/project/extractionstring)
 - the official git repository is on [https://framagit.org/nlp/extractionstring](https://framagit.org/nlp/extractionstring)
 - the official documentation is on [https://nlp.frama.io/extractionstring/](https://nlp.frama.io/extractionstring/)
 

## Philosophy of this library

In `extractionstring`, one thinks of a string as a collection of integers: the position of each character in the string. For instance

```python
'Simple string for demonstration and for illustration.' # the parent string
'01234567891123456789212345678931234567894123456789512' # the positions

'       string                       for illustration ' # the ExtractionString es
'       789112                       678 412345678951 ' # the associated positions

'Simple                                               ' # the ExtractionString es2
'012345                                               ' # the associated positions
```

To define the `ExtractionString` `'string for illustration'` consists in selecting the positions `[7,13, 36,39, 40,52]` from the parent string, and the `ExtractionString` `'simple'` is defined by the positions `[0,6,]`. 

In addition, one can see the above ranges as sets of positins. Then it is quite easy to perform some basic operations on the `Span`, for instance the addition of two `ExtractionString`

```python
str(es1 + es2) = 'Simple string for illustration'
```

is interpreted as the union of their relative sets of positions.

In addition to these logical operations, there are a few utilities, like the possibility to split or slice a `ExtractionString` object, as long as their are all related to the same parent string.

## Basic example

Below we give a simple example of usage of the `ExtractionString` class.

```python
import re
from extractionstring import ExtractionString

string = 'Simple string for demonstration and for illustration.'
initial_span = ExtractionString(string)

# char-gram generation
chargrams = initial_span.slice(0, len(initial_span), 3)
str(chargrams[2])
# return 'mpl'

# each char-gram conserves a memory of the initial string
chargrams[2].string
# return 'Simple string for demonstration and for illustration.'

cuts = []
for r in re.finditer(r'\W+', string):
    cuts += [r.start(), r.end()]
spans = initial_span.split(cuts)
# this returns a list of ExtractionString objects
# representing the tokens as if string.split() was applied


# an other possibility to keep only the words is to construct it explicitly
cuts = []
for r in re.finditer(r'\w+', string):
    cuts += [r.start(), r.end()]
spans = ExtractionString(string, intervals=cuts).extractions
# extractions attribute contains the list of sub-tokens

# 2-gram construction
ngram = [ExtractionString(string, intervals=cuts[2*i:2*i+4]) 
         for i in range(len(cuts)//2-1)]
ngram[2]
# return ExtractionString('for demonstration', [(14,17),(18,31)])
str(ngram[2])
# return 'for demonstration'
ngram[2].intervals
# return EvenSizedSortedSet[(14,17);(18,31)]
ngram[2].extractions
# return [ExtractionString('for', [(14,17)]), ExtractionString('demonstration', [(18,31)])]

# are the two 'for' Token the same ?
spans[2] == spans[-2]
# return False, because they are not at the same position

# basic operations among Token
for_for = spans[2] + spans[-2]
str(for_for)
# return 'for for'
for_for.intervals
# return EvenSizedSortedSet[(14,17);(36,39)]
for_for.string
# return 'Simple string for demonstration and for illustration.'
# to check the positions of the two 'for' ExtractionString : 
#        '01234567890...456...01234567890.....67890............'

# also available : 
# span1 + span2 : union of the sets of span1.intervals and span2.intervals
# span1 - span2 : difference of span1.intervals and span2.intervals
# span1 * span2 : intersection of span1.intervals and span2.intervals
# span1 / span2 : symmetric difference of span1.intervals and span2.intervals

```

Other examples can be found in the [documentation](https://nlp.frama.io/extractionstring/).

## Comparison with other Python libraries

A comparison with some other NLP librairies (nltk, gensim, spaCy, gateNLP, ...) can be found in the [documentation](https://nlp.frama.io/extractionstring/tutorials/comparison_other_libraries.html)

## Installation

Simply run 

```bash
pip install extractionstring
```

should install the library from Python Package Index (PIP). The official repository is on https://framagit.org/nlp/extractionstring. To install the package from the repository, run the following command lines 

```bash
git clone https://framagit.org/nlp/extractionstring.git
cd extractionstring/
pip install .
```

Once installed, one can run some tests using

```bash
cd tests/
python3 -m unittest -v
```

(verbosity `-v` is an option).

## Versions

See [CHANGES file](CHANGES.md) in this folder.

## About us

Package developped for Natural Language Processing at IAM : Unité d'Informatique et d'Archivistique Médicale, Service d'Informatique Médicale, Pôle de Santé Publique, Centre Hospitalo-Universitaire (CHU) de Bordeaux, France.

You are kindly encouraged to contact the authors by issue on the [official repository](https://framagit.org/nlp/extractionstring/-/issues/), and to propose ameliorations and/or suggestions to the authors, via issue or merge requests.

Last version : Jan 3, 2023