import sys
import os
import unittest

sys.path.append(os.path.abspath(".."))



from codewars.Dbautista.codewars_tasks_8kyu import square_or_square_root as impl1
from codewars.mpeshko.ky8 import square_or_square_root as impl2
from codewars.TYakushevych.ky8 import square_or_square_root as impl3
from codewars.YuliaShap.kyu8 import square_or_square_root as impl4

class TestSquareOrSquareRoot(unittest.TestCase):
    
    arr1 = [4, 3, 9, 7, 2, 1 ]
    arr2 = [100, 101, 5, 5, 1, 1]
    arr3 = [1, 2, 3, 4, 5, 6]
    res1 = [2, 9, 3, 49, 4, 1]
    res2 = [10, 10201, 25, 25, 1, 1]
    res3 = [1, 4, 9, 2, 25, 36]


    def test_Dbautista(self):
        self.assertEqual(impl1(self.arr1), self.res1)
        self.assertEqual(impl1(self.arr2), self.res2)
        self.assertEqual(impl1(self.arr3), self.res3)
    
    def test_mpeshko(self):
        self.assertEqual(impl2(self.arr1), self.res1)
        self.assertEqual(impl2(self.arr2), self.res2)
        self.assertEqual(impl2(self.arr3), self.res3)
        
    def test_TYakushevych(self):
        self.assertEqual(impl3(self.arr1), self.res1)
        self.assertEqual(impl3(self.arr2), self.res2)
        self.assertEqual(impl3(self.arr3), self.res3)
        
    def test_YuliaShap(self):
        self.assertEqual(impl4(self.arr1), self.res1)
        self.assertEqual(impl4(self.arr2), self.res2)
        self.assertEqual(impl4(self.arr3), self.res3)
            
if __name__ == '__main__':
    unittest.main()