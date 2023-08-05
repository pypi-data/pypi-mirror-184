#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tools to sort the ExtractionString.s. All the methods works for any objects having order relations, in particular they work for `EvenSizedSortedSet` as well.

Sorting (as given by the `sort` method below) correspond to a sorting with respect to the `start` attribute of the object in increasing, and if several starts are the same, then the sorting uses the `stop` attribute in increasing order.
"""
from typing import List
from itertools import permutations

import numpy as np

from .extraction_string import ExtractionString

relations_weights = {
    "__lt__": -2,
    "__gt__": +2,
    "__le__": -1,
    "__ge__": +1,
}


def order_weight(es1: ExtractionString, es2: ExtractionString) -> int:
    """Calculate the ordering weight between es1 and es2, two `ExtractionString` instances."""
    weight = 0
    for rel, w in relations_weights.items():
        weight += w if getattr(es1, rel)(es2) else 0
    return weight


def order_matrix(extraction_strings: List[ExtractionString]) -> np.array:
    """Construct the order matrix from a list of `ExtractionString`. Returns an antisymmetric matrix (a `numpy` array) of integers."""
    orders = np.zeros(
        shape=(len(extraction_strings), len(extraction_strings)), dtype=np.int8
    )
    for i, j in permutations(range(len(extraction_strings)), 2):
        orders[i, j] = order_weight(extraction_strings[i], extraction_strings[j])
    return orders


def sort_by_weight(
    extraction_strings: List[ExtractionString],
) -> List[ExtractionString]:
    """Sort the list of `ExtractionString` by the order given by the `relations_weights`."""
    extraction_strings_ordmat = order_matrix(extraction_strings)
    nb_gt = [sum(line[line > 0]) for line in extraction_strings_ordmat]
    extraction_strings_sorted = [extraction_strings[i] for i in np.argsort(nb_gt)]
    return extraction_strings_sorted


def sort(extraction_strings: List[ExtractionString]) -> List[ExtractionString]:
    """Sort by the `start` attribute, then by the `stop` attribute."""
    return sorted(extraction_strings, key=lambda x: (x.start, x.stop))
