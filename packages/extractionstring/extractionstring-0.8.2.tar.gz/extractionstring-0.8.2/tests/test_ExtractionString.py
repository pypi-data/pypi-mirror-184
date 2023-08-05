#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test of the ESSSerlappingIntervals class

Run as 

python3 -m unittest -v tests.test_ExtractionString

from the parent folder
"""

import unittest as ut

from extractionstring.extraction_string import ExtractionString 
from extractionstring.even_sized_sorted_set import EvenSizedSortedSet as ESSS

string = ''.join(f'{i}123456789' for i in range(10))

class TestExtractionString(ut.TestCase):
    
    def test_attributes(self):
        """string, intervals and subtoksep are present in the class instance"""
        es = ExtractionString()
        self.assertEqual(es.string, str())
        self.assertEqual(es.intervals, ESSS())
        self.assertEqual(es.subtoksep, ' ')
        with self.assertRaises(AttributeError):
            es.encoding
        es = ExtractionString(string,
                              subtoksep='_')
        self.assertEqual(es.string, string)
        self.assertEqual(str(es), string)
        self.assertEqual(es.intervals, ESSS(0,len(string)))
        self.assertEqual(es.subtoksep, '_')
        es = ExtractionString(es)
        self.assertEqual(es.string, string)
        self.assertEqual(str(es), string)
        self.assertEqual(es.intervals, ESSS(0,len(string)))
        self.assertEqual(es.subtoksep, '_')
        return None 
    
    def test_relative2absolute(self):
        """mapping between the positions in the extracted string and the original one, positions in the subtksep are represented by None"""
        es = ExtractionString(string)
        r2a = {i:i for i in range(len(string))}
        self.assertEqual(es.relative2absolute, r2a)
        es = ExtractionString(string,
                              intervals=(0,10,20,30),
                              subtoksep='__')
        r2a = {i:i for i in range(10)}
        r2a.update({i+10:None for i in range(2)})
        r2a.update({i+12:20+i for i in range(10)}) 
        self.assertEqual(es.relative2absolute, r2a) 
        return None
    
    def test_remove_append(self):
        es = ExtractionString(string)
        es.remove(10,20)
        self.assertEqual(es.intervals, ESSS(0,10,20,100))
        es.remove(10,20)
        self.assertEqual(es.intervals, ESSS(0,10,20,100))
        es.remove(30,40)
        self.assertEqual(es.intervals, ESSS(0,10,20,30,40,100))
        es.append(30,40)
        self.assertEqual(es.intervals, ESSS(0,10,20,100))
        es.append(10,20)
        self.assertEqual(es.intervals, ESSS(0,100))
        return None 
    
    def test_order_relations_non_overlapping(self):
        es = ExtractionString(string)
        es.remove(10,20)
        es1 = es.get_extraction(0)
        es2 = es.get_extraction(1)
        with self.assertRaises(IndexError):
            es.get_extraction(2) 
        self.assertTrue(es1 < es2)
        self.assertFalse(es1 <= es2)
        self.assertFalse(es1 > es2)
        self.assertFalse(es1 >= es2)
        self.assertFalse(es2 < es1)
        self.assertFalse(es2 <= es1)
        self.assertTrue(es2 > es1)
        self.assertFalse(es2 >= es1)
        return None 
    
    def test_set_methods(self):
        es = ExtractionString(string)
        es1 = es.copy() 
        es1.intervals = ESSS(10,30)
        es2 = es.copy()
        es2.intervals = ESSS(20,40)
        # difference
        es = es1 - es2
        self.assertEqual(es.intervals, ESSS(10,20))
        self.assertEqual(str(es), '1123456789')
        es = es2 - es1
        self.assertEqual(es.intervals, ESSS(30,40))
        self.assertEqual(str(es), '3123456789')
        # intersection
        es = es1 * es2
        self.assertEqual(es.intervals, ESSS(20,30))
        self.assertEqual(str(es), '2123456789')
        es = es2 * es1
        self.assertEqual(es.intervals, ESSS(20,30))
        self.assertEqual(str(es), '2123456789')
        # union
        es = es1 + es2
        self.assertEqual(es.intervals, ESSS(10,40))
        self.assertEqual(str(es), '112345678921234567893123456789')   
        es = es2 + es1
        self.assertEqual(es.intervals, ESSS(10,40))
        self.assertEqual(str(es), '112345678921234567893123456789')
        # symmetric difference
        es = es1 / es2
        self.assertEqual(es.intervals, ESSS(10,20,30,40))
        self.assertEqual(str(es), '1123456789 3123456789')  
        es = es2 / es1
        self.assertEqual(es.intervals, ESSS(10,20,30,40))
        self.assertEqual(str(es), '1123456789 3123456789')
        return None 
    
    def test_extract(self):
        es = ExtractionString(string) 
        self.assertEqual(str(es), es.string)
        part = es.extract(10,90) 
        self.assertEqual(str(part), es.string[10:90])
        part = es.extract(20,80) 
        self.assertEqual(str(part), es.string[20:80])
        part = part.extract(10,30) 
        self.assertEqual(str(part), es.string[30:50]) 
        self.assertEqual(str(es), es.string) 
        p1 = es.extract(10,20) 
        p2 = es.extract(50,60) 
        p3 = es.extract(80,90) 
        part = p1 + p2 + p3 
        self.assertEqual(part.intervals, ESSS(10,20,50,60,80,90))
        p = part.extract(5,10) 
        self.assertEqual(str(p), '56789')
        self.assertEqual(p.intervals, ESSS(15,20))
        p = part.extract(5,11) 
        self.assertEqual(str(p), '56789 ')
        self.assertEqual(p.intervals, ESSS(15,20).append_empty(-1))
        p = part.extract(5,15) 
        self.assertEqual(str(p), '56789 5123')
        self.assertEqual(p.intervals, ESSS(15,20,50,54))
        p = part.extract(10,15) 
        self.assertEqual(str(p), ' 5123')
        self.assertEqual(p.intervals, ESSS(50,54).append_empty(0))
        p = part.extract(5,25) 
        self.assertEqual(str(p), '56789 5123456789 812')
        self.assertEqual(p.intervals, ESSS(15,20,50,60,80,83)) 
        es = ExtractionString(string, intervals=(0,1,5,15)) 
        es.extract(0,2)
        es.extract(1,10)
        return None     
    
    def test_partition(self):
        es = ExtractionString(string) 
        part = es.partition(10,20) 
        self.assertEqual(part[0].intervals, ESSS(0,10)) 
        self.assertEqual(str(part[0]), '0123456789') 
        self.assertEqual(part[0].string, string) 
        self.assertEqual(part[1].intervals, ESSS(10,20)) 
        self.assertEqual(str(part[1]), '1123456789') 
        self.assertEqual(part[1].string, string) 
        self.assertEqual(part[2].intervals, ESSS(20,100)) 
        self.assertEqual(str(part[2]), ''.join(f'{i}123456789' for i in range(2,10))) 
        self.assertEqual(part[2].string, string) 
        part = part[-1].partition(10,20) 
        self.assertEqual(part[0].intervals, ESSS(20,30)) 
        self.assertEqual(str(part[0]), '2123456789') 
        self.assertEqual(part[0].string, string)
        self.assertEqual(part[1].intervals, ESSS(30,40))
        self.assertEqual(str(part[1]), '3123456789') 
        self.assertEqual(part[1].string, string)
        self.assertEqual(part[2].intervals, ESSS(40,100)) 
        self.assertEqual(str(part[2]), ''.join(f'{i}123456789' for i in range(4,10))) 
        self.assertEqual(part[2].string, string)
        # on multiple intervals
        sub = es.copy() 
        sub.intervals = ESSS(20,30,40,50)
        self.assertEqual(str(sub), '2123456789 4123456789') 
        self.assertEqual(sub.string, string) 
        part = sub.partition(5,15) 
        self.assertEqual(part[0].intervals, ESSS(20,25)) 
        self.assertEqual(str(part[0]), '21234') 
        self.assertEqual(part[0].string, string)
        self.assertEqual(part[1].intervals, ESSS(25,30,40,44))
        self.assertEqual(str(part[1]), '56789 4123') 
        self.assertEqual(part[1].string, string)
        self.assertEqual(part[2].intervals, ESSS(44,50)) 
        self.assertEqual(str(part[2]), '456789') 
        self.assertEqual(part[2].string, string) 
        part = sub.partition(5,10) 
        self.assertEqual(part[0].intervals, ESSS(20,25)) 
        self.assertEqual(str(part[0]), '21234') 
        self.assertEqual(part[0].string, string)
        self.assertEqual(part[1].intervals, ESSS(25,30))
        self.assertEqual(str(part[1]), '56789') 
        self.assertEqual(part[1].string, string)
        self.assertEqual(part[2].intervals, ESSS(40,50).append_empty(0)) 
        self.assertEqual(str(part[2]), ' 4123456789') 
        self.assertEqual(part[2].string, string)
        return None
    
    def test_split(self):
        """split a string such that the inner parts of the given intervals are withdrawn"""
        es = ExtractionString(string) 
        part = es.split((10,20,30,40,50,60,70,80)) 
        self.assertEqual(len(part), 5)
        self.assertEqual(str(part[0]), '0123456789')
        self.assertEqual(part[0].intervals, ESSS(0,10))
        self.assertEqual(str(part[1]), '2123456789')
        self.assertEqual(part[1].intervals, ESSS(20,30))
        self.assertEqual(str(part[2]), '4123456789')
        self.assertEqual(part[2].intervals, ESSS(40,50))
        self.assertEqual(str(part[3]), '6123456789')
        self.assertEqual(part[3].intervals, ESSS(60,70))
        self.assertEqual(str(part[4]), '81234567899123456789')
        self.assertEqual(part[4].intervals, ESSS(80,100)) 
        # with right boundary
        part = es.split((10,100)) 
        self.assertEqual(len(part), 1)
        self.assertEqual(str(part[0]), '0123456789')
        self.assertEqual(part[0].intervals, ESSS(0,10))
        # with left boundary 
        part = es.split((0,90)) 
        self.assertEqual(len(part), 1)
        self.assertEqual(str(part[0]), '9123456789')
        self.assertEqual(part[0].intervals, ESSS(90,100))
        # with splitted span
        es = ExtractionString(string, intervals=(10,20,30,40,50,60)) 
        part = es.split((5,10,20,21,27,32)) 
        self.assertEqual(len(part), 3)
        self.assertEqual(str(part[0]), '11234')
        self.assertEqual(part[0].intervals, ESSS(10,15))
        self.assertEqual(str(part[1]), ' 312345678') 
        self.assertEqual(part[1].intervals, ESSS(30,39).append_empty(0))
        self.assertEqual(str(part[2]), ' 51234')
        self.assertEqual(part[2].intervals, ESSS(50,55).append_empty(0))
        part = es.split((0,10,11,21)) 
        self.assertEqual(len(part), 2)
        self.assertEqual(str(part[0]), ' ')
        self.assertEqual(part[0].intervals, ESSS().append_empty(0).append_empty(0))
        self.assertEqual(str(part[1]), ' 5123456789')
        self.assertEqual(part[1].intervals, ESSS(50,60).append_empty(0))
        return None 
        
    def test_slice(self):
        """Slice a string"""
        es = ExtractionString(string) 
        part = es.slice(start=0, stop=25, size=1, step=1)
        for i,s in enumerate(part):
            self.assertEqual(str(s), string[i])
        part = es.slice(start=0, stop=25, size=1, step=2) 
        for i,s in enumerate(part):
            self.assertEqual(str(s), string[2*i])
        part = es.slice(start=12, stop=25, size=2, step=4) 
        for i,s in enumerate(part):
            self.assertEqual(str(s), string[12+4*i:14+4*i])


