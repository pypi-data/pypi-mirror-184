# Tokenization for language processing

This package contains some basic tools allowing to cut a string in sub-parts (cf. [Wikipedia](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization)), called `Token`.

`iamtokenizing` classes allow basic tokenization of text, such as

 - word splitting, n-gram splitting, (using `NGrams` class) 
 - char-gram splitting of arbitrary size (using `CharGrams` class). 

`NGrams` also accepts any REGular EXpression (REGEX) to match pattern that will serve as splitting string. The class `RegexDetector` also allows to extract the REGEX pattern as token. In addition, `ContextDetector` allow to split text on some REGEX, and to detect inside these splits an other REGEX, keeping some organisation (called context) of the text between the two detection and splitting scales.

## Installation

 - The documentation is available on [https://nlp.frama.io/iamtokenizing/](https://nlp.frama.io/iamtokenizing/)
 - The PyPi package is available on [https://pypi.org/project/iamtokenizing/](https://pypi.org/project/iamtokenizing/)
 - The official repository is on [https://framagit.org/nlp/iamtokenizing](https://framagit.org/nlp/iamtokenizing)

### From Python Package Index (PIP)

Simply run 

```bash
pip install iamtokenizing
```

is sufficient.

### From the repository

The official repository is on https://framagit.org/nlp/iamtokenizing

Once the repository has been downloaded (or cloned), one can install this package using `pip` : 

```bash
git clone https://framagit.org/nlp/iamtokenizing.git
cd iamtokenizing/
pip install .
```

Once installed, one can run some tests using

```bash
cd tests/
python3 -m unittest -v
```

(verbosity `-v` is an option).

## Basic examples

Basic examples can be found in the [documentation](https://nlp.frama.io/iamtokenizing/).

## Versions

 - Versions before 0.4 only present the `Token` and `Tokens` classes. They have been splitted after in three classes, named `Span`, `Token` and `Tokens`. Importantly, the methods `Token.append` and `Token.remove` no longer exist in the next version. They have been replaced by `Token.append_range`, `Token.append_ranges`, `Token.remove_range` and `Token.remove_ranges`.
 - Version 0.4 add the class `Span` to `Token` and `Tokens`. `Span` handles the sub-parts splitting of a given string, whereas `Token` and `Tokens` now consumes `Span` objects and handle the attributes of the `Token`. 
 - From version 0.5, one has split the basic tools `Span`, `Token` and `Tokens` from the `iamtokenizing` package (see https://pypi.org/project/iamtokenizing/). Only the advanced tokenizer are now present in the package `iamtokenizing`, which depends on the package `tokenspan`. The objects `Span`, `Token` and `Tokens` can be called as before from the newly deployed package `tokenspan`, available on https://pypi.org/project/tokenspan/.

## About us

Package developped for Natural Language Processing at IAM : Unité d'Informatique et d'Archivistique Médicale, Service d'Informatique Médicale, Pôle de Santé Publique, Centre Hospitalo-Universitaire (CHU) de Bordeaux, France.

You are kindly encouraged to flag any trouble, and to propose ameliorations and/or suggestions to the authors, via issue or merge requests.

Last version : August 6, 2021