from labsupport import *
from lab02 import *

TEST_IntKaratsuba   = True
TEST_PolyKaratsuba  = True
TEST_BinPowMod      = True

class Lab02Tester(LabTester):
    
    #region Тесты для функции IntKaratsuba.

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_IntKaratsuba, 'TEST_IntKaratsuba = False')
    def test_IntKaratsuba_Sample(self):
        """Тестирование функции IntKaratsuba фиксированным набором входных параметров."""
        
        sample = [(2, 11), (0, 0), (1, 5), (5, 1), (377, 122), (122, 377), (78961234, 97641234), (1356789, 1356789), (-123, 1356789), (-876, 407), (2123123145, 81223), (123125958, 0), (0, -23425200)]

        for e in sample: self.Check_IntKaratsuba_At(*e)

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_IntKaratsuba, 'TEST_IntKaratsuba = False')
    def test_IntKaratsuba_RandomSample(self):
        """Тестирование функции IntKaratsuba большим набором случайных входных параметров."""
        
        for i in range(1000):
            e = map(int, random.randint(-10**7, 10**7 + 1, 2))
            self.Check_IntKaratsuba_At(*e)

    def Check_IntKaratsuba_At(self, a, b):
        r = self.Call_Function_Gently(IntKaratsuba, (a, b))
        self.assertEqual(r, a * b, GetIncorrectResultMessage(IntKaratsuba, (a, b)))            

    #endregion

    #region Тесты для функции PolyKaratsuba.

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_PolyKaratsuba, 'TEST_PolyKaratsuba = False')
    def test_PolyKaratsuba_RandonSample(self):
        """Тестирование функции PolyKaratsuba набором случайных входных параметров."""

        for i in range(100):
            a, b =  RandPolyCoefficients(20), RandPolyCoefficients(20)
            self.Check_PolyKaratsuba_At((a, b))

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_PolyKaratsuba, 'TEST_PolyKaratsuba = False')
    def test_PolyKaratsuba_Sample(self):
        """Тестирование функции PolyKaratsuba фиксированным набором входных параметров."""
        
        sample = [([1, 2, 3], [1, 1]), ([4, 0, -7], [2, 1, -1, 7]), ([0], [0]), ([-1], [22]), ([-1], [2, 0, 8]), ([1, 0, 0], [4, 1, 3, 4]), ([2, -1, -11], [11, 13, 0, 0, 0]), ([0], [-13, 137, -124, -27, -6, -95, 180, -30, 53, 164, 108, -187, 38, -193, -194, 26, -40])]

        for e in sample: self.Check_PolyKaratsuba_At(e)

    def Check_PolyKaratsuba_At(self, params):
        a, b = map(numpy.array, params)

        r1 = self.Call_Function_Gently(PolyKaratsuba, (a, b))
        r2 = numpy.trim_zeros(numpy.polymul(a, b), 'f')

        if not len(r2): r2 = numpy.array([0])

        numpy.testing.assert_array_equal(r1, r2, GetIncorrectResultMessage(PolyKaratsuba, params))

    #endregion

    #region Тесты для функции BinPowMod.

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_BinPowMod, 'TEST_BinPowMod = False')
    def test_BinPowMod_Sample(self):
        """Тестирование функции BinPowMod фиксированным набором входных параметров."""

        sample = [(10, 10, 2, 0), (5, 3, 13, 8), (13, 0, 3, 1), (1, 117, 3, 1), (4, 13, 497, 445), (595, 703, 991, 342), (175, 235, 257, 3), (2, -1, 4, None), (3, -1, 4, 3), (3, -2, 4, 1), (2, -11, 25, 12), (2, -2, 5, 4), (3, -2, 7, 4), (5, -3, 11, 3)]

        for a, p, n, r in sample: self.Check_BinPowMod_At((a, p, n), r)

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_BinPowMod, 'TEST_BinPowMod = False')
    def test_BinPowMode_RandomSample(self):
        """Тестирование функции BinPowMod большим набором случайных входных параметров."""
        
        for i in range(1000):
            p = tuple(map(int, random.randint(2, 1001, 3)))
            self.Check_BinPowMod_At(p, pow(*p))

    def Check_BinPowMod_At(self, params, expected_r):
        r = self.Call_Function_Gently(BinPowMod, params)
        self.assertEqual(r, expected_r, GetIncorrectResultMessage(BinPowMod, params))

    #@unittest.skip("temporarily")
    @unittest.skipUnless(TEST_BinPowMod, 'TEST_BinPowMod = False')
    def test_BinPowMod_Exceptions(self):
        """Тестирование функции BinPowMod на предмет генерирования исключения ValueError при n = 0."""
        
        self.assertRaises(ValueError, self.Call_Function_Gently, BinPowMod, (10, 13, 0), ValueError)
        self.assertRaises(ValueError, self.Call_Function_Gently, BinPowMod, (20, 37, 0), ValueError)

    #endregion

if __name__ == '__main__':
    unittest.main(failfast = True)