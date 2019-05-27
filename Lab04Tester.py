from labsupport import *
from lab04 import PolyInverseModOverQ, PolyInverseModOverZn, PolyDivModOverQ, PolyDivModOverZn

TEST_PolyInverseModOverQ    = True
TEST_PolyInverseModOverZn   = True
TEST_PolyDivModOverQ        = True
TEST_PolyDivModOverZn       = True

class Lab04Tester(LabTester):

    #region Тесты для функции PolyInverseModOverZn.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyInverseModOverZn, 'TEST_PolyInverseModOverZn = False')
    def test_PolyInverseModOverZn_Sample(self):
        """Тестирование функции PolyInverseModOverZn фиксированным набором входных параметров."""

        sample = [([1, 2, 3, 7, 8, 9, -2], 4, 11), ([1, 2, 0, 1, -1], 4, 12), ([4, 9, -7, 1, 2, -3, 5], 5, 15), ([1, -2, 2, -8], 1, 3), ([3, 1, 2, 4, -1, 0, 1], 2, 8), ([1, 2, 1], 100, 3), ([89, 1], 6, 10), ([0, 1, 2, 3], 2, 3), ([1, 2, 3, 4, 5], 3, 1), ([0], 17, 7), ([2, 4, 5], 2, 8), ([3, 0, 0, 1], 2, 9), ([-186, 132, -63, 64, 46, 47, -61, 74, -33, 168, 104, 116, 38, 187, 90], 17, 8)]
        
        for e in sample:
            self.Check_PolyInverseModOverZn_At(*e)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyInverseModOverZn, 'TEST_PolyInverseModOverZn = False')
    def test_PolyInverseModOverZn_RandomSample(self):
        """Тестирование функции PolyInverseModOverZn большим набором случайных входных параметров."""

        for i in range(100):
            r, n = random.randint(1, 20, 2)
            f = RandPolyCoefficients(20)

            self.Check_PolyInverseModOverZn_At(f, r, n)

        for i in range(50):
            f = RandPolyCoefficients(20)
            jcf = abs(f[0])

            if jcf == 1: n = 1
            elif not jcf:
                n = random.randint(1, 20)
            else:
                factors = primes(jcf)
                l = len(factors)
                k = random.randint(0, l)
                r, m = random.randint(1, 20, 2)
                n = factors[k] * m

            self.Check_PolyInverseModOverZn_At(f, r, n)

        for i in range(25):
            f, r = RandPolyCoefficients(20), random.randint(1, 20)

            self.Check_PolyInverseModOverZn_At(f, r, 1)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyInverseModOverZn, 'TEST_PolyInverseModOverZn = False')
    def test_PolyInverseModOverZn_Exceptions(self):
        """Тестирование функции PolyInverseModOverZn на предмет генерирования исключения ValueError при r < 1 или n < 1."""

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (unitpoly, 1, 0), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (zeropoly, 5, -1), ValueError)

        n = random.randint(-1000, 1)
        f = Polynomial(RandPolyCoefficients(99))

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (f, 500, n), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (unitpoly, 0, 3), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (zeropoly, -3, 2), ValueError)

        r = random.randint(-1000, 1)
        f = PolynomialInQ(RandPolyCoefficients(99))

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (f, r, 1), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverZn, (zeropoly, -3, -2), ValueError)

    def Check_PolyInverseModOverZn_At(self, f, r, n):
        result = self.Call_Function_Gently(PolyInverseModOverZn, (Polynomial(f), r, n))

        message = GetIncorrectResultMessage(PolyInverseModOverZn, (f, r, n))

        if invmod(f[0], n) is not None:
            o = PolynomialMod((result * f).truncate(r), n)
            self.assertEqual(o, unitpoly, message)
        else:
            self.assertIsNone(result, message)

    #endregion

    #region Тесты для функции PolyInverseModOverQ.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyInverseModOverQ, 'TEST_PolyInverseModOverQ = False')
    def test_PolyInverseModOverQ_Sample(self):
        """Тестирование функции PolyInverseModOverQ фиксированным набором входных параметров."""

        sample = [([1, 2, 3, 7, 8, 9, -2], 4), ([1, 2, 0, 1, -1], 4), ([4, 9, -7, 1, 2, -3, 5], 5), ([1, -2, 2, -8], 1), ([3, 1, 2, 4, -1, 0, 1], 2), ([1, 2, 1], 100), ([89, 1], 6), ([0, 1, 2, 3], 2), ([0, -1, 2, 3, -11, 17, 36], 4)]

        for e in sample:
            self.Check_PolyInverseModOverQ_At(*e)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyInverseModOverQ, 'TEST_PolyInverseModOverQ = False')
    def test_PolyInverseModOverQ_RandomSample(self):
        """Тестирование функции PolyInverseModOverQ большим набором случайных входных параметров."""

        for i in range(100):
            r = random.randint(1, 20)
            f = RandPolyCoefficients(20)

            self.Check_PolyInverseModOverQ_At(f, r)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyInverseModOverQ, 'TEST_PolyInverseModOverQ = False')
    def test_PolyInverseModOverQ_Exceptions(self):
        """Тестирование функции PolyInverseModOverQ на предмет генерирования исключения ValueError при r < 1."""

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverQ, (unitpoly, 0), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverQ, (zeropoly, -3), ValueError)

        r = random.randint(-1000, 1)
        f = PolynomialInQ(RandPolyCoefficients(99))

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyInverseModOverQ, (f, r), ValueError)
    
    def Check_PolyInverseModOverQ_At(self, f, r):
        result = self.Call_Function_Gently(PolyInverseModOverQ, (PolynomialInQ(f), r))

        message = GetIncorrectResultMessage(PolyInverseModOverQ, (f, r))

        if f[0]:
            o = (result * f).truncate(r).trim()
            self.assertEqual(o, unitpoly, message)
        else:
            self.assertIsNone(result, message)

    #endregion

    #region Тесты для функции PolyDivModOverQ.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyDivModOverQ, 'TEST_PolyDivModOverQ = False')
    def test_PolyDivModOverQ_Sample(self):
        """Тестирование функции PolyDivModOverQ фиксированным набором входных параметров."""

        sample = [([1, 2, 3, 7, 8, 9, -2], [1, 2, 0, 1, -1]), ([4, 9, -7, 1, 2, -3, 5], [1, -2, 2, -8]), ([1, 2, -1, 0, 1, 18], [0, 1, 2, -4]), ([0, 1, 3, -11, 27], [0, 0, 27]), ([1, 2, 3], [4, 5, 6, 7, 8, 9]), ([1, 9, 3, 0, 0], [1, 2, 3, 4]), ([9, 3, 5, -1], [0]), ([5, 4, -1, -11], [0, 0, 0]), ([0, -197, 186, 14, -103, -107, -194], [-122]), ([0, 0, 0, -197, 186, 14, -103, -107, -194], [-122])]

        for o in sample:
            self.Check_PolyDivModOverQ_At(o)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyDivModOverQ, 'TEST_PolyDivModOverQ = False')
    def test_PolyDivModOverQ_RandomSample(self):
        """Тестирование функции PolyDivModOverQ большим набором случайных входных параметров."""
        
        for i in range(100):
            params = RandPolyCoefficients(30), RandPolyCoefficients(30)

            self.Check_PolyDivModOverQ_At(params)

    def Check_PolyDivModOverQ_At(self, params):
        p = tuple(map(PolynomialInQ, params))

        if any(params[1]):
            result = self.Call_Function_Gently(PolyDivModOverQ, p)

            self.assertEqual(result, divmod(*p), GetIncorrectResultMessage(PolyDivModOverQ, params))
        else:
            with self.assertRaises(ZeroDivisionError):
                self.Call_Function_Gently(PolyDivModOverQ, p, ZeroDivisionError)

    #endregion

    #region Тесты для функции PolyDivModOverZn.

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyDivModOverZn, 'TEST_PolyDivModOverZn = False')
    def test_PolyDivModOverZn_Sample(self):
        """Тестирование функции PolyDivModOverZn фиксированным набором входных параметров."""

        sample = [([1, 2, 3, 7, 8, 9, -2], [1, 2, 0, 1, -1], 11), ([4, 9, -7, 1, 2, -3, 5], [1, -2, 2, -8], 13), ([1, 2, -1, 0, 1, 18], [0, 1, 2, -4], 19), ([0, 1, 3, -11, 27], [0, 0, 27], 29), ([1, 2, 3], [4, 5, 6, 7, 8, 9], 11), ([1, 9, 3, 0, 0], [1, 2, 3, 4, 17], 19), ([9, 3, 5, -1], [0], 37), ([5, 4, -1, -11], [0, 0, 0], 13), ([0, -197, 186, 14, -103, -107, -194], [-122], 5), ([0, 0, 0, -197, 186, 14, -103, -107, -194], [-122], 5), ([1, 2, 4, 5], [3, 4], 8), ([1, 2], [2, 3, 6], 18), ([2, 3, 6], [1, 2, 3], 18), ([1, 0, 0, 2], [2, 7], 21), ([-145, 182, 23, -132, 13,  159, -186, -49, -69, -98, -95, -24, -88, 69, -186, 5, 190, 76, 118, -108, -33, -28.], [-197, 0], 86)]

        for params in sample:
            self.Check_PolyDivModOverZn_At(*params)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyDivModOverZn, 'TEST_PolyDivModOverZn = False')
    def test_PolyDivModOverZn_RandomSample(self):
        
        for i in range(100):
            n = random.randint(1, 100)
            ab = RandPolyCoefficients(40), RandPolyCoefficients(40)

            self.Check_PolyDivModOverZn_At(*ab, n)

        for i in range(25):
            b = RandPolyCoefficients(40, 1)
            a = RandPolyCoefficients(2 * len(b), len(b))
            lcb = abs(b[-1])

            if lcb == 1:
                n = lcb
            elif lcb:                
                factors = primes(lcb)
                l = len(factors)
                k = random.randint(0, l)
                n = factors[k]

            self.Check_PolyDivModOverZn_At(a, b, n)

        for i in range(25):
            b = RandPolyCoefficients(40)
            a = RandPolyCoefficients(2 * len(b), len(b))

            self.Check_PolyDivModOverZn_At(a, b, 1)

    def Check_PolyDivModOverZn_At(self, a, b, n):
        a, b = Polynomial(a), Polynomial(b)
        ta, tb = PolynomialMod(a, n), PolynomialMod(b, n)

        if ta.degree() < tb.degree() or invmod(tb.coef[-1], n) is not None:
            q, r = self.Call_Function_Gently(PolyDivModOverZn, (a, b, n))

            message = GetIncorrectResultMessage(PolyDivModOverZn, (a, b, n))

            self.assertEqual(PolynomialMod(ta, n), PolynomialMod(q * tb + r, n), message)
            self.assertTrue(r.degree() < b.degree() or r == zeropoly, message)
        else:
            with self.assertRaises(ZeroDivisionError):
                self.Call_Function_Gently(PolyDivModOverZn, (a, b, n), ZeroDivisionError)

    #@unittest.skip('temporarily')
    @unittest.skipUnless(TEST_PolyDivModOverZn, 'TEST_PolyDivModOverZn = False')
    def test_PolyDivModOverZn_Exceptions(self):
        """Тестирование функции PolyDivModOverZn на предмет генерирования исключения ValueError при n < 1."""

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyDivModOverZn, (zeropoly, unitpoly, 0), ValueError)

        with self.assertRaises(ValueError):
            self.Call_Function_Gently(PolyDivModOverZn, (unitpoly, zeropoly, -11), ValueError)

        n = random.randint(-10000, 1)
        ab = RandPolyCoefficients(30), RandPolyCoefficients(30)

        self.assertRaises(ValueError, self.Call_Function_Gently, PolyDivModOverZn, (*ab, n), ValueError)

    #endregion

if __name__ == '__main__':
    unittest.main(failfast = True)