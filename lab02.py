import numpy as np
from lab01 import GCD



# def is_degree_of_2(a):
#     while a > 1:
#         if a & 1 == 1:
#             return False
#         a >>= 1
#     return True

def IntKaratsuba(a: int, b: int):
    def bin_len(num: int):
        if num == 0:
            return 1
        res = 0
        while num:
            num >>= 1
            res += 1
        return res

    def Karatsuba_rec(a: int, b: int, n: int):
        if n <= 1:
            return a & b
        else:
            if n & 1:
                n += 1
            m = n // 2

            F1 = a >> m
            F0 = a & ((1 << m) - 1)
            G1 = b >> m
            G0 = b & ((1 << m) - 1)

            k1 = Karatsuba_rec(F1, G1, m)
            k0 = Karatsuba_rec(F0, G0, m)
            U = IntKaratsuba(F0 + F1, G0 + G1)
            k_u = U - k1 - k0
            return (k1 << n) + (k_u << m) + k0

    m1, m2 = (a < 0), (b < 0)
    a, b = abs(a), abs(b)
    n = max(a.bit_length(), b.bit_length())

    res = Karatsuba_rec(a, b, n)
    if m1 ^ m2:
        return -res
    else:
        return res

def PolyKaratsuba(a: np.array, b: np.array):
    def split_poly(poly: np.array, m: int):
        if len(poly) > m:
            return poly[0: len(poly) - m], poly[len(poly) - m: m*2]
        else:
            return np.array([]), poly

    def Karatsuba_rec(poly1: np.array, poly2: np.array, n: int):
        if (len(poly1) == 0) or (len(poly2) == 0):
            return np.array([0])
        if n == 1:
            return poly1 * poly2
        else:
            if n & 1:
                n += 1
            m = n // 2
            #F1, F0 = poly1[:m], poly1[m:]
            F1, F0 = split_poly(poly1, m)
            G1, G0 = split_poly(poly2, m)

            k1 = Karatsuba_rec(F1, G1, m)
            k0 = Karatsuba_rec(F0, G0, m)
            U = Karatsuba_rec(np.polyadd(F0, F1), np.polyadd(G0, G1), m)
            k_u = np.polysub(np.polysub(U, k0), k1)

            k1 = np.concatenate([k1, np.zeros(n)])
            k_u = np.concatenate([k_u, np.zeros(m)])
            return np.polyadd(np.polyadd(k1, k0), k_u)

    n = max(len(a), len(b))
    res = Karatsuba_rec(a, b, n)
    i = 0
    while (i < len(res)) and (res[i] == 0):
        i += 1
    res = res[i: len(res)]
    if len(res) == 0:
        return np.array([0])
    return res

def BinPowMod(a: int, p: int, n: int):
    if (a == 0) and (p == 0):
        return None
    if (a < 0) or (n < 1):
        raise ValueError
    a %= n
    if p < 0:
        if GCD(a, n)[0] != 1:
            return None
        f_n = 0
        for i in range(1, n):
            if GCD(i, n)[0] == 1:
                f_n += 1
        p = p % f_n

    res = 1
    while p > 0:
        if p & 1 == 1:
            res = (res * a) % n
        a = (a * a) % n
        p >>= 1
    return res % n
