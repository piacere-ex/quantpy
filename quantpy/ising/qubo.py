# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:sts=4:et:ai:ff=unix:fenc=utf-8

"""
"""

#get ising matrix from qubo
import numpy as np

def getMat(qubo):
    N = len(qubo)
    h = []
    J = [[0]*N for i in range(N)]
    Jsum = 0
    hsum = 0

    for j in range(N):
        sum = 0

        for i in range(j+1,N):
                r = qubo[j][i]
                sum += r
                J[j][i] = r*1.0/4
                J[i][j] = r*1.0/4
                Jsum += r*1.0/4

        for i in range(0,j):
                sum += qubo[j][i]

        s = qubo[j][j]
        hsum += s*1.0/2
        h.append(s*1.0/2 + sum)

    return np.array([h,J,Jsum+hsum])