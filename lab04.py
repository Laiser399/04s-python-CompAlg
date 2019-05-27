from numpy.polynomial.polynomial import Polynomial as Poly
from lab01 import InverseMod
from math import log, log2, ceil
import numpy as np


def PolyInverseModOverQ(f: Poly, r: int) -> Poly:
    if r < 1:
        raise ValueError
    if f.coef[0] == 0:
        return None
    g = Poly([1 / f.coef[0]])
    k = ceil(log(r, 2))
    deg = 1
    for i in range(k):
        g = 2 * g - f * g * g
        deg *= 2
        g = g.cutdeg(deg - 1)
    return g

def PolyCoefMod(f: Poly, n: int) -> Poly:
    res = f.copy()
    for i in range(len(res.coef)):
        res.coef[i] = res.coef[i] % n
    return res

def PolyInverseModOverZn(f: Poly, r: int, n: int) -> Poly:
    if (r < 1) or (n < 1):
        raise ValueError
    g = InverseMod(f.coef[0], n)
    if g is None:
        return None
    g = Poly([g])
    k = ceil(log2(r))
    deg = 1
    for i in range(k):
        g = 2 * g - f * g * g
        deg *= 2
        g = g.cutdeg(deg - 1)
        g = PolyCoefMod(g, n)
    #g = g.cutdeg(r - 1)
    return g


def rev(f: Poly, k: int) -> Poly:
    f = f.trim()
    if k < f.degree():
        return None
    res = Poly(f.coef[::-1])
    if k > f.degree():
        res = Poly(np.concatenate([np.zeros(k - f.degree()), res.coef]))
    return res.trim()

def PolyDivModOverQ(a: Poly, b: Poly) -> (Poly, Poly):
    a = a.trim(); b = b.trim()
    da, db = a.degree(), b.degree()
    if da < db:
        return Poly([0]), a
    #q = PolyInverseModOverQ(rev(b, db), b.degree() + 1)
    q = PolyInverseModOverQ(rev(b, db), max(b.degree() + 1, a.degree() + 1))
    if q is None:
        raise ZeroDivisionError

    q = rev(a, da) * q
    q = q.cutdeg(da - db)
    q = rev(q, da - db)
    r = a - q * b

    return q, r

def PolyDivModOverZn(a: Poly, b: Poly, n: int) -> (Poly, Poly):
    if n < 1:
        raise ValueError
    a, b = PolyCoefMod(a, n), PolyCoefMod(b, n)
    a = a.trim(); b = b.trim()

    da, db = a.degree(), b.degree()
    if da < db:
        return (Poly([0]), a)
    q = PolyInverseModOverZn(rev(b, db), max(b.degree() + 1, a.degree() + 1), n)
    #q = PolyInverseModOverZn(rev(b, db), b.degree() + 1, n)
    if q is None:
        raise ZeroDivisionError
    q = rev(a, da) * q
    q = q.cutdeg(da - db)
    q = rev(q, da - db)
    r = a - q * b

    q, r = PolyCoefMod(q, n), PolyCoefMod(r, n)
    q = q.trim(); r = r.trim()

    return q, r
