import math
from sympy import gcdex, Poly
from sympy.abc import x
from labsupport import *
from lab01 import *

TEST_GCD        = True
TEST_PolyGCD    = True
TEST_InverseMod = True

def XGCD(a : Polynomial, b : Polynomial):
    _a, _b = Poly(a.coef[::-1], x), Poly(b.coef[::-1], x)

    if _b == 0:
        _a, _b = _b, _a

    s, t, g = gcdex(_a, _b)

    return Polynomial(g.all_coeffs()[::-1])

class Lab01Tester(LabTester):

    #region Тесты для функций GCD и GCD_rec.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_GCD, 'TEST_GCD = False')
    def test_GCD_Sample(self):
        """Тестирование функций GCD и GCD_rec фиксированным набором входных параметров."""

        sample = [(2, 10), (1, -10), (3, 10), (3, 15), (4, 2), (5, 4), (1000, 0), (17, 11), (23, 9), (119, 7), (137, 5), (-22, 33), (25, 15), (34, 51), (-15, -10), (-14, 35), (14, -35)]

        for e in sample:
            self.Check_GCD_At(e)

        self.assertEqual(GCD_rec(0, 0), (None, None, None), GetIncorrectResultMessage(GCD_rec, (0, 0)))
        self.assertEqual(GCD(0, 0), (None, None, None), GetIncorrectResultMessage(GCD, (0, 0)))

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_GCD, 'TEST_GCD = False')
    def test_GCD_RandomSample(self):
        """Тестирование функций GCD и GCD_rec большим набором случайных входных параметров."""

        for i in range(1000):
            # Due to the following warning: RuntimeWarning: overflow encountered in long_scalars.
            e = tuple(map(numpy.int64, random.randint(1, 1000001, 2)))
            self.Check_GCD_At(e)

    def Check_GCD_At(self, e):
        self.Check_GCDFunction_At(*e, GCD_rec, math.gcd)
        self.Check_GCDFunction_At(*e, GCD, math.gcd)

    def Check_GCDFunction_At(self, a, b, f, builtin_f):
        g, x, y = self.Call_Function_Gently(f, (a, b))
        gcd = builtin_f(a, b)

        message = GetIncorrectResultMessage(f, (a, b))

        self.assertEqual(gcd, g, message)
        self.assertEqual(a * x + b * y, g, message)

    #endregion

    #region Тесты для функций PolyGCD и PolyGCD_rec.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyGCD, 'TEST_PolyGCD = false')
    def test_PolyGCD_Sample(self):
        """Тестирование функций PolyGCD и PolyGCD_rec фиксированным набором входных параметров."""

        sample = [([1, 1], [1, 0, -1]), ([1, 1], [1, -1]), ([1, 1, 1], [1, 0, 1, 0, 1]), ([2, -3, 9], [7, -22, 3]), ([-9, -3, 2], [3, -22, 7]), ([11, -17, -37], [2, 4, 8, 10]), ([0], [1, 2, 3]), ([-1, -2, -3], [0]), ([0, -63, -68, 128, 143], [7, -50, -6, 91])]

        for e in sample:
            self.Check_PolyGCD_At(tuple(map(PolynomialInQ, e)))
        
        self.assertEqual(PolyGCD(zeropoly, zeropoly), (None, None, None), GetIncorrectResultMessage(PolyGCD, (zeropoly, zeropoly)))
        self.assertEqual(PolyGCD_rec(zeropoly, zeropoly), (None, None, None), GetIncorrectResultMessage(PolyGCD_rec, (zeropoly, zeropoly)))

    def Check_PolyGCD_At(self, e):
        self.Check_GCDFunction_At(*e, PolyGCD_rec, XGCD)
        self.Check_GCDFunction_At(*e, PolyGCD, XGCD)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyGCD, 'TEST_PolyGCD = false')
    def test_PolyGCD_RandomSample(self):
        """Тестирование функций PolyGCD и PolyGCD_rec большим набором случайных входных параметров."""

        for i in range(30):
            a = PolynomialInQ(RandPolyCoefficients(20))
            b = PolynomialInQ(RandPolyCoefficients(20))
            c = PolynomialInQ(RandPolyCoefficients(20))

            self.Check_PolyGCD_At((a * c, b * c))

        for i in range(30):
            a = PolynomialInQ(RandPolyCoefficients(15))
            b = PolynomialInQ(RandPolyCoefficients(10))

            self.Check_PolyGCD_At((a, b))

    #endregion

    #region Тесты для функции InverseMod.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_InverseMod, 'TEST_InverseMod = False')
    def test_InverseMod_Sample(self):
        """Тестирование функции InverseMod фиксированным набором входных параметров."""

        sample = [(2, 3), (2, 4), (5, 7), (11, 13), (7, 9), (5, 17), (5, 21), (17, 34)]

        for e in sample:
            self.Check_InverseMod_At(e)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_InverseMod, 'TEST_InverseMod = False')
    def test_InverseMod_RandomSample(self):
        """Тестирование функции InverseMod большим набором случайных входных параметров."""

        for i in range(1000):
            e = tuple(random.randint(1, 10001, 2))
            self.Check_InverseMod_At(e)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_InverseMod, 'TEST_InverseMod = False')
    def test_InverseMod_Exceptions(self):
        """Тестирование функции InverseMod на предмет генерирования исключения ValueError при n = 0."""
        
        with self.assertRaises(ValueError):
            self.Call_Function_Gently(InverseMod, (5, 0), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(InverseMod, (2, 0), ValueError)

        for i in range(5):
            with self.assertRaises(ValueError):
                a = random.randint(1, 10001)
                self.Call_Function_Gently(InverseMod, (a, 0), ValueError)

    def Check_InverseMod_At(self, params):
        r = self.Call_Function_Gently(InverseMod, params)
        self.assertEqual(r, invmod(*params), GetIncorrectResultMessage(InverseMod, params))

    #endregion

if __name__ == '__main__':
    unittest.main(failfast = True)