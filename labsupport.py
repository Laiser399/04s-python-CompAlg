from numpy.polynomial.polynomial import Polynomial
from fractions import Fraction
from sympy import mod_inverse
from numpy import random, mod
import inspect, unittest, sys
import __main__, os, hashlib, numpy
from pathlib import Path

class LabTester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = __main__.__file__
        print("\nPath: %s\nMD5: %s\t%s\nMD5: %s\t%s\n" % (path, cls.getFileMD5(path), cls.getFileSHA1(path), cls.getFileMD5(__file__), cls.getFileSHA1(__file__)))

    @classmethod
    def getFileMD5(cls, path):
        path = os.path.abspath(path)
        content = Path(path).read_text().encode('utf-8')
        md5 = hashlib.md5()

        md5.update(content)

        return md5.hexdigest()

    @classmethod
    def getFileSHA1(cls, path):
        path = os.path.abspath(path)
        content = Path(path).read_text().encode('utf-8')
        sha1 = hashlib.sha1()

        sha1.update(content)

        return sha1.hexdigest()

    def Call_Function_Gently(self, f, params, expected_ex : Exception = None):
        happened_ex = None

        try:
            result = f(*params)
        except Exception as ex:
            happened_ex = ex

            if expected_ex is not None and isinstance(ex, expected_ex):
                raise

            self.fail(GetUnexpectedErrorMessage(f, params))
        finally:
            if happened_ex is None and expected_ex is not None:
                sys.stderr.write(GetParamsString(f, params))

        return result

    # def assertEqual(self, first, second, params):
    #     super().assertEqual(first, second, params)

# class DivisionWithRemainderError(ZeroDivisionError):
#     pass

zeropoly = Polynomial(0)
unitpoly = Polynomial(1)

PolynomialInQ = lambda l: Polynomial([Fraction(o) for o in l])

PolynomialMod = lambda p, n: Polynomial(mod(p.coef, n)).trim()

def RandPolyCoefficients(max_degree, min_degree : int = 0):
    if min_degree > max_degree:
        raise ValueError

    n = random.randint(min_degree, max_degree + 1) + 1 if max_degree else 1

    return random.randint(-200, 201, n).tolist() # Why the hell should this work so?

def GetParamsString(f, params):
    fs = '\n'

    for i in range(len(inspect.signature(f).parameters)):
        fs += f.__code__.co_varnames[i][0] + ' = %s\n'

    return fs % params

def GetNoExpectedErrorMessage(f, params, exception):
    return '\nФункция %s не вызвала исключения %s.\n\nПараметры:\n%s' % (f.__name__, exception, GetParamsString(f, params))

def GetUnexpectedErrorMessage(f, params):
    return '\nВходе выполнения функции %s произошло непредвиденное исключение.\nСм. внутреннее исключение.\n\nПараметры:%s' % (f.__name__, GetParamsString(f, params))

def GetIncorrectResultMessage(f, params):
    return '\nФункция %s вернула некорректное значение.\n\nПараметры:%s' % (f.__name__, GetParamsString(f, params))

# в какой-то версии работает некорректно
def invmod(a : int, n : int):
    try:
        r = mod_inverse(int(a), int(n))
    except ValueError:
        return None
    return r

def primes(n : int) -> list:
    r, i = [], 2

    while i * i <= n:
        while n % i == 0:
            r.append(i)
            n //= i
        i += 1

    if n > 1:
       r.append(n)

    return r