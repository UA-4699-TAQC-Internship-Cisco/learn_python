import sys
import os
import unittest

sys.path.append(os.path.abspath(".."))



from codewars.Dbautista.codewars_tasks_5kyu import perimeter as impl1
from codewars.mpeshko.ky5 import perimeter as impl2
from codewars.TYakushevych.ky5 import perimeter as impl3
from codewars.YuliaShap.kyu5 import perimeter as impl4

class TestFindNb(unittest.TestCase):
    insert1 = 0
    insert2 = 5
    insert3 = 7
    insert4 = 20
    insert5 = 30
    insert6 = 100
    insert7 = 500
    res1 = 4
    res2 = 80
    res3 = 216
    res4 = 114624
    res5 = 14098308
    res6 = 6002082144827584333104
    res7 = 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504


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