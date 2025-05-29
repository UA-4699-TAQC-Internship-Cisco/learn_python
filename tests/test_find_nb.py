import sys
import os
import unittest

sys.path.append(os.path.abspath(".."))



from codewars.Dbautista.codewars_tasks_6kyu import find_nb as impl1
from codewars.mpeshko.ky6 import find_nb as impl2
from codewars.TYakushevych.ky6 import find_nb as impl3
from codewars.YuliaShap.kyu6 import find_nb as impl4

class TestFindNb(unittest.TestCase):
    insert1 = 4
    insert2 = 16
    insert3 = 4183059834009
    insert4 = 24723578342962
    insert5 = 135440716410000
    insert6 = 40539911473216
    insert7 = 26825883955641
    res1 = -1
    res2 = -1
    res3 = 2022
    res4 = -1
    res5 = 4824
    res6 = 3568
    res7 = 3218


    def test_Dbautista(self):
        self.assertEqual(impl1(self.insert1), self.res1)
        self.assertEqual(impl1(self.insert2), self.res2)
        self.assertEqual(impl1(self.insert3), self.res3)
        self.assertEqual(impl1(self.insert4), self.res4)
        self.assertEqual(impl1(self.insert5), self.res5)
        self.assertEqual(impl1(self.insert6), self.res6)
        self.assertEqual(impl1(self.insert7), self.res7)
    
    def test_mpeshko(self):
        self.assertEqual(impl2(self.insert1), self.res1)
        self.assertEqual(impl2(self.insert2), self.res2)
        self.assertEqual(impl2(self.insert3), self.res3)
        self.assertEqual(impl2(self.insert4), self.res4)
        self.assertEqual(impl2(self.insert5), self.res5)
        self.assertEqual(impl2(self.insert6), self.res6)
        self.assertEqual(impl2(self.insert7), self.res7)
        
    def test_TYakushevych(self):
        self.assertEqual(impl3(self.insert1), self.res1)
        self.assertEqual(impl3(self.insert2), self.res2)
        self.assertEqual(impl3(self.insert3), self.res3)
        self.assertEqual(impl3(self.insert4), self.res4)
        self.assertEqual(impl3(self.insert5), self.res5)
        self.assertEqual(impl3(self.insert6), self.res6)
        self.assertEqual(impl3(self.insert7), self.res7)
        
    def test_YuliaShap(self):
        self.assertEqual(impl4(self.insert1), self.res1)
        self.assertEqual(impl4(self.insert2), self.res2)
        self.assertEqual(impl4(self.insert3), self.res3)
        self.assertEqual(impl4(self.insert4), self.res4)
        self.assertEqual(impl4(self.insert5), self.res5)
        self.assertEqual(impl4(self.insert6), self.res6)
        self.assertEqual(impl4(self.insert7), self.res7)
            
if __name__ == '__main__':
    unittest.main()