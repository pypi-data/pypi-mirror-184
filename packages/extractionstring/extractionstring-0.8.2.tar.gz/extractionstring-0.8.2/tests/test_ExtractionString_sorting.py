#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test of the ExtractionString class

Run as 

python3 -m unittest -v tests.test_ExtractionString_sorting

from the parent folder.
"""

from random import shuffle

import unittest as ut

from extractionstring.extraction_string import ExtractionString
from extractionstring import sorting

string = ''.join(f'{i}123456789' for i in range(10))

class TestExtractionStringSorting(ut.TestCase):
    
    def test_non_overlapping(self):
        """Non-overlapping sorting"""
        ess, starts, stops = [], [], []
        for i in range(5):
            start, stop = i*10, (i+1)*10-1
            es = ExtractionString(string, intervals=(start, stop))
            ess.append(es)
            starts.append(start)
            stops.append(stop)
        ess.insert(1,ExtractionString(string))
        starts.insert(1,0)
        stops.insert(1,len(string))
        shuffle(ess)
        sorted_ess = sorting.sort(ess)
        sorting.order_matrix(ess)
        for es, start, stop in zip(sorted_ess, starts, stops):
            self.assertEqual(es.start, start)
            self.assertEqual(es.stop, stop)
        return None 
    
    def test_slicing_contiguous(self):
        """Sort some slicing extractions of contiguous intervals"""
        ess, starts, stops = [], [], []
        for i in range(15):
            start, stop = i, i+5
            es = ExtractionString(string, intervals=(start, stop))
            ess.append(es)
            starts.append(start)
            stops.append(stop)
        ess.insert(1,ExtractionString(string))
        starts.insert(1,0)
        stops.insert(1,len(string))
        shuffle(ess)
        sorted_ess = sorting.sort(ess)
        for es, start, stop in zip(sorted_ess, starts, stops):
            self.assertEqual(es.start, start)
            self.assertEqual(es.stop, stop)
        return None 

    def test_slicing_noncontiguous(self):
        """Sort some slicing extractions of non-contiguous intervals"""
        ess, starts, stops = [], [], []
        for i in range(15):
            intervals = (i, i+5, i+7, i+10)
            es = ExtractionString(string, intervals=intervals)
            ess.append(es)
            starts.append(intervals[0])
            stops.append(intervals[-1])
        ess.insert(1,ExtractionString(string))
        starts.insert(1,0)
        stops.insert(1,len(string))
        shuffle(ess)
        sorted_ess = sorting.sort(ess)
        for es, start, stop in zip(sorted_ess, starts, stops):
            self.assertEqual(es.start, start)
            self.assertEqual(es.stop, stop)
        return None 

    def test_overlapping_longer_and_longer(self):
        """Sort some overlapping extractions all starting at the same position, and having longer and longer length"""
        ess, starts, stops = [], [], []
        for i in range(2,15):
            intervals = (0, i)
            es = ExtractionString(string, intervals=intervals)
            ess.append(es)
            starts.append(intervals[0])
            stops.append(intervals[-1])
        shuffle(ess)
        sorted_ess = sorting.sort(ess)
        for es, start, stop in zip(sorted_ess, starts, stops):
            self.assertEqual(es.start, start)
            self.assertEqual(es.stop, stop)
        return None 

    def test_slicing_longer_and_longer(self):
        """Sort some overlapping extractions having incresing starting position as in slice, and having longer and longer length"""
        ess, starts, stops = [], [], []
        for i in range(8):
            for j in range(5):
                intervals = (i, i+j+1)
                es = ExtractionString(string, intervals=intervals)
                ess.append(es)
                starts.append(intervals[0])
                stops.append(intervals[-1])
        shuffle(ess)
        sorted_ess = sorting.sort(ess)
        for es, start, stop in zip(sorted_ess, starts, stops):
            self.assertEqual(es.start, start)
            self.assertEqual(es.stop, stop)
        return None 