"""
Test of the NonOverlappingIntervals class

Run as 

python3 -m unittest -v tests.test_NonOverlappingIntervals

from the parent folder
"""

import unittest as ut

from extractionstring.non_overlapping_intervals import NonOverlappingIntervals

string = ''.join(str(i)+'123456789' for i in range(10))

# # for construction
# class Empty(): pass
# self = Empty()

class TestNonOverlappingIntervals(ut.TestCase):

    def test_len(self,):
        """Returns half the total length of the input datas"""
        for stop in range(13,28,4):
            intervals = list(range(2,stop,2))
            noi = NonOverlappingIntervals(*intervals)
            self.assertEqual(len(noi), len(intervals)//2)
        return None
    
    def test_getitem(self,):
        """Verify noi.list, list(noi), [x for x in noi], noi[i] and noi[i:j] methods, and equality"""
        intervals = list(range(2,13,2))
        slices = [slice(start, stop) for start, stop in zip(intervals[:-1:2],
                                                            intervals[1::2])]
        noi = NonOverlappingIntervals(*intervals)
        self.assertEqual(noi.list, intervals)
        list_noi = list(noi)
        self.assertEqual(list_noi, slices)
        list_noi = [sl for sl in noi]
        self.assertEqual(list_noi, slices)
        list_noi = [noi[i] for i in range(len(noi))]
        self.assertEqual(list_noi, slices)
        self.assertEqual(noi[:1], NonOverlappingIntervals(*intervals[:2]))
        self.assertEqual(noi[:2], NonOverlappingIntervals(*intervals[:-2]))
        self.assertEqual(noi[1:], NonOverlappingIntervals(*intervals[2:]))
        self.assertEqual(noi[2:], NonOverlappingIntervals(*intervals[4:]))
        self.assertEqual(noi[:-1], NonOverlappingIntervals(*intervals[:-2]))
        self.assertEqual(noi[:-2], NonOverlappingIntervals(*intervals[:-4]))
        self.assertEqual(noi[::2], NonOverlappingIntervals(*(intervals[0:2]+intervals[4:6])))
        self.assertEqual(noi[1::2], NonOverlappingIntervals(*intervals[2:4]))
        
        noi = NonOverlappingIntervals()
        with self.assertRaises(IndexError):
            noi.start
        with self.assertRaises(IndexError):
            noi.stop 
        return None 

        
if __name__ == '__main__':
    ut.main()
