from numpy.polynomial.polynomial import Polynomial as Poly
import numpy as np
from lab01 import InverseMod
from lab04 import PolyInverseModOverZn, PolyDivModOverZn, rev, PolyCoefMod

# i) f_inv = [6 59 14 31]
# ii) q = [77 16 17 37 79]   r = [12 71 25]

n = 101
a = Poly([37, 36, 35, 34, 33, 32, 31, 30])
b = Poly([20, 19, 18, 17])
f = rev(b, 3)
f_inv = PolyInverseModOverZn(f, 4, n)

q, r = PolyDivModOverZn(a, b, n)







