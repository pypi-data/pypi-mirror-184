"""
Test of the NonOverlappingPositions class

Run as 

python3 -m unittest -v tests.test_NonOverlappingPositions

from the parent folder
"""

import unittest as ut

from extractionstring.non_overlapping_positions import NonOverlappingPositions

string = ''.join(str(i)+'123456789' for i in range(10))

# # for construction
# class Empty(): pass
# self = Empty()

class TestNonOverlappingPositions(ut.TestCase):

    def test_len(self,):
        """Returns half the total length of the input datas"""
        for stop in range(13,28,4):
            intervals = list(range(2,stop,2)) # add two more positions at each stop loop
            noi = NonOverlappingPositions(*intervals)
            self.assertEqual(len(noi), stop//2)
        return None
    
    def test_getitem(self,):
        """Verify noi.list, list(noi), [x for x in noi], noi[i] and noi[i:j] methods, and equality"""
        intervals = list(range(2,13,2))
        positions = [i for start, stop in zip(intervals[:-1:2], intervals[1::2]) 
                     for i in range(start, stop)]
        noi = NonOverlappingPositions(*intervals)
        self.assertEqual(noi.list, intervals)
        list_noi = list(noi)
        self.assertEqual(list_noi, positions)
        list_noi = [sl for sl in noi]
        self.assertEqual(list_noi, positions)
        list_noi = [noi[i] for i in range(len(noi))]
        self.assertEqual(list_noi, positions)
        self.assertEqual(noi, intervals)
        self.assertEqual(noi[:1], [2,])
        self.assertEqual(noi[:2], [2,3])
        self.assertEqual(noi[1:], [3, 6, 7, 10, 11])
        self.assertEqual(noi[2:], [6, 7, 10, 11])
        self.assertEqual(noi[:-1], [2, 3, 6, 7, 10])
        self.assertEqual(noi[:-2], [2, 3, 6, 7])
        self.assertEqual(noi[::2], [2, 6, 10])
        self.assertEqual(noi[1::2], [3, 7, 11])
        
        noi = NonOverlappingPositions()
        with self.assertRaises(IndexError):
            noi.start
        with self.assertRaises(IndexError):
            noi.stop 
        return None 

        
if __name__ == '__main__':
    ut.main()
