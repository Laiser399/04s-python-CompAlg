from numpy import polydiv, polysub, polymul, polyadd
import numpy




def GCD(a: int, b: int):
    if (a == 0) and (b == 0):
        return [None, None, None]
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return [a, x, y]

def GCD_rec(a: int, b: int):
    def rec(a: int, b: int):
        if b == 0:
            return [a, 1, 0]
        else:
            tm = GCD_rec(b, a % b)
            return [tm[0], tm[2], tm[1] - a // b * tm[2]]
    if (a == 0) and (b == 0):
        return [None, None, None]
    return rec(a, b)

def isZeroPoly(p: numpy.array):
    for i in p:
        if i != 0:
            return False
    return True

def PolyGCD(a: numpy.array, b: numpy.array):
    if isZeroPoly(a) and isZeroPoly(b):
        return [None, None, None]
    x, xx, y, yy = numpy.array([1]), numpy.array([0]), numpy.array([0]), numpy.array([1])
    while not isZeroPoly(b):
        q = polydiv(a, b)

        a, b = b, q[1]
        x, xx = xx, polysub(x, polymul(xx, q[0]))
        y, yy = yy, polysub(y, polymul(yy, q[0]))
    return [a, x, y]

def PolyGCD_rec(a: numpy.array, b: numpy.array):
    def rec(a: numpy.array, b: numpy.array):
        if isZeroPoly(b):
            return [a, numpy.array([1]), numpy.array([0])]
        else:
            q = polydiv(a, b)
            tm = PolyGCD_rec(b, q[1])
            return [tm[0], tm[2], polysub(tm[1], polymul(q[0], tm[2]))]
    if isZeroPoly(a) and isZeroPoly(b):
        return [None, None, None]
    return rec(a, b)

def InverseMod(a: int, n: int):
    if n <= 1:
        return None
    x, a, b = GCD(a, n)
    if x == 1:
        return a % n
    else:
        return None








