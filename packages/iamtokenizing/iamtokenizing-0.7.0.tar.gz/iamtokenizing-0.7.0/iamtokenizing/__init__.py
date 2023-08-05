#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("iamtokenizing").version
except DistributionNotFound:
    __version__ = AttributeError("installation is required for versionning")

from .base_tokenizer import BaseTokenizer
from .ngrams import NGrams
from .chargrams import CharGrams
from .regex_detector import RegexDetector
from .context_detector import ContextDetector
