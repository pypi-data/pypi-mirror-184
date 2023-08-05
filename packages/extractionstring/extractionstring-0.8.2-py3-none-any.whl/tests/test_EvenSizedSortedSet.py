"""
Test of the EvenSizedSortedSet class

Run as 

python3 -m unittest -v tests.test_EvenSizedSortedSet

from the parent folder
"""

import unittest as ut

from extractionstring.even_sized_sorted_set import EvenSizedSortedSet

string = ''.join(str(i)+'123456789' for i in range(10))

# # for construction
# class Empty(): pass
# self = Empty()

class TestEvenSizedSortedSet(ut.TestCase):
    
    def setUp(self):
        self.list = [5,3,6,1,9,12]
        self.nor = EvenSizedSortedSet(*self.list)
        return None
    
    def test_appendSimple(self,):
        """Append an interval to a NOI"""
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(1,25)
        self.assertTrue(nor.list == [1,25])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(25,28)
        self.assertTrue(nor.list == sorted(intervals) + [25,28])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(4,5)
        self.assertTrue(nor.list == [1,3,4,6,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(6,7)
        self.assertTrue(nor.list == [1,3,5,7,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(0,2)
        self.assertTrue(nor.list == [0,3,5,6,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(3,7)
        self.assertTrue(nor.list == [1,7,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.append(3,5)
        self.assertTrue(nor.list == [1,6,9,12])
        return None

    def test_removeSimple(self,):
        """Remove an interval from a NOI"""
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(1,25)
        self.assertTrue(nor.list == [])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(25,28)
        self.assertTrue(nor.list == sorted(intervals))
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(4,5)
        self.assertTrue(nor.list == [1,3,5,6,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(6,7)
        self.assertTrue(nor.list == [1,3,5,6,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(0,2)
        self.assertTrue(nor.list == [2,3,5,6,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(3,7)
        self.assertTrue(nor.list == [1,3,9,12])
        intervals = [5,3,6,1,9,12]
        nor = EvenSizedSortedSet(*intervals)
        nor.remove(3,5)
        self.assertTrue(nor.list == [1,3,5,6,9,12])
        return None
    
    def test_contains_start_stop(self,):
        """.start, .stop and __contains__ methods"""
        intervals = list(range(2,13,2))
        noi = EvenSizedSortedSet(*intervals)
        self.assertEqual(noi.start, intervals[0])
        self.assertEqual(noi.stop, intervals[-1])
        for start, stop in noi:
            for i in range(start, stop):
                self.assertTrue(i in noi)
            self.assertTrue(EvenSizedSortedSet(start, stop) in noi)
        return None
    
    def test_interval_index(self):
        """get the index of the interval where the position belongs"""
        intervals = list(range(0,21,4))
        noi = EvenSizedSortedSet(*intervals) 
        expected_indices = [0, 0, 0, 0, 
                            None, None, None, None,
                            1, 1, 1, 1, 
                            None, None, None, None,
                            2, 2, 2, 2, 
                            None,]
        for e_ind, position in zip(expected_indices, range(22)):
            index = noi.interval_index(position, outside_index=None)
            assert e_ind == index 
            self.assertTrue( e_ind == index )
        return None 
        
    def test_ordering_when_non_overlapping(self,):
        """The order operations"""
        noi1 = EvenSizedSortedSet(2,6)
        noi2 = EvenSizedSortedSet(9,12)
        self.assertTrue(noi1 < noi2)
        self.assertFalse(noi1 > noi2)
        self.assertFalse(noi1 <= noi2)
        self.assertFalse(noi1 >= noi2)
        self.assertFalse(noi2 < noi1)
        self.assertTrue(noi2 > noi1)
        self.assertFalse(noi2 <= noi1)
        self.assertFalse(noi2 >= noi1)
        return None

    
    def test_ordering_when_edge_in_common(self,):
        """The order operations when the intervals have one edge in common, still not overlapping"""
        noi1 = EvenSizedSortedSet(2,9)
        noi2 = EvenSizedSortedSet(9,12)
        self.assertTrue(noi1 < noi2)
        self.assertFalse(noi1 > noi2)
        self.assertFalse(noi1 <= noi2)
        self.assertFalse(noi1 >= noi2)
        self.assertFalse(noi2 < noi1)
        self.assertTrue(noi2 > noi1)
        self.assertFalse(noi2 <= noi1)
        self.assertFalse(noi2 >= noi1)
        return None 

    def test_ordering_when_partly_overlapping(self,):
        """The order operations when the intervals are partly overlapping"""
        noi1 = EvenSizedSortedSet(2,9)
        noi2 = EvenSizedSortedSet(8,12)
        self.assertFalse(noi1 < noi2)
        self.assertFalse(noi1 > noi2)
        self.assertTrue(noi1 <= noi2)
        self.assertFalse(noi1 >= noi2)
        self.assertFalse(noi2 < noi1)
        self.assertFalse(noi2 > noi1)
        self.assertFalse(noi2 <= noi1)
        self.assertTrue(noi2 >= noi1)
        return None 

    def test_ordering_when_totally_overlapping(self,):
        """The order operations when the intervals completely overlapping"""
        noi1 = EvenSizedSortedSet(2,9)
        noi2 = EvenSizedSortedSet(1,12)
        self.assertFalse(noi1 < noi2)
        self.assertFalse(noi1 > noi2)
        self.assertFalse(noi1 <= noi2)
        self.assertTrue(noi1 >= noi2)
        self.assertFalse(noi2 < noi1)
        self.assertFalse(noi2 > noi1)
        self.assertTrue(noi2 <= noi1)
        self.assertFalse(noi2 >= noi1)
        return None 

    def test_set_operations(self,):
        """The order operations when the intervals completely overlapping"""
        intervals = list(range(2,13,2))
        noi = EvenSizedSortedSet(*intervals)
        noi1 = EvenSizedSortedSet(2,4,10,12) # the two edges NOI
        noi2 = EvenSizedSortedSet(6,8) # the interior NOI
        # intersection
        self.assertEqual(noi.intersection(noi2), noi2)
        self.assertEqual(noi2.intersection(noi), noi2)
        self.assertEqual(noi2*noi, noi2)
        self.assertEqual(noi*noi2, noi2)
        # union
        self.assertEqual(noi1.union(noi2), noi)
        self.assertEqual(noi2.union(noi1), noi)
        self.assertEqual(noi2+noi1, noi)
        self.assertEqual(noi1+noi2, noi)
        # difference
        empty_noi = EvenSizedSortedSet()
        self.assertEqual(noi.difference(noi2), noi1)
        self.assertEqual(noi2.difference(noi), empty_noi)
        self.assertEqual(noi.difference(noi1), noi2)
        self.assertEqual(noi1.difference(noi), empty_noi)
        self.assertEqual(noi-noi2, noi1)
        self.assertEqual(noi-noi1, noi2)
        self.assertEqual(noi1-noi2, noi1)
        self.assertEqual(noi2-noi1, noi2)
        # symmetric_difference
        self.assertEqual(noi.symmetric_difference(noi2), noi1)
        self.assertEqual(noi2.symmetric_difference(noi), noi1)
        self.assertEqual(noi.symmetric_difference(noi1), noi2)
        self.assertEqual(noi1.symmetric_difference(noi), noi2)
        self.assertEqual(noi/noi1, noi2)
        self.assertEqual(noi1/noi, noi2)
        self.assertEqual(noi/noi2, noi1)
        self.assertEqual(noi2/noi, noi1)
        self.assertEqual(noi1/noi2, noi)
        self.assertEqual(noi2/noi1, noi)
        return None 
        
if __name__ == '__main__':
    ut.main()
