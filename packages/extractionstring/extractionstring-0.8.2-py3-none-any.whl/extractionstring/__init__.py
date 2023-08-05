#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("extractionstring").version
except DistributionNotFound:
    __version__ = AttributeError("installation is required for versionning")

from .even_sized_sorted_set import EvenSizedSortedSet
from .non_overlapping_intervals import NonOverlappingIntervals
from .non_overlapping_positions import NonOverlappingPositions
from .extraction_string import ExtractionString
