from lab01 import GCD
from lab02 import BinPowMod

import numpy as np

def getEmptyMtx(dim: int):
    mtx = np.empty((dim, dim))
    # for i in range(dim):
    #     mtx.append([])
    #     for j in range(dim):
    #         mtx[i].append(0)
    return mtx

def calcDFT(val, n):
    mtx = getEmptyMtx(n)
    for row in range(n):
        for column in range(n):
            if (row == 0) or (column == 0):
                mtx[row][column] = 1
            else:
                mtx[row][column] = BinPowMod(val, row * column, n)
    return mtx

def funcEuler(n: int):
    res = 0
    for i in range(1, n):
        if GCD(i, n)[0] == 1:
            res += 1
    return res

def task_i():
    s = set()
    for i in range(1, 29):
        s.add(BinPowMod(i, 7, 29))
    return s

a = 12
mtx = calcDFT(12, 29)
print(mtx)
if np.linalg.det(mtx) != 0:
    mtx_inv = np.linalg.inv(mtx)
    res = np.dot(mtx, mtx_inv)
else:
    print("det = 0")








