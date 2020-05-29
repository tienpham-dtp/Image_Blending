'''
  File name: getCoefficientMatrix.py
  Author: Tien Pham
  Date created: 10/1/2019
'''

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
import scipy.sparse.linalg
from scipy.sparse.linalg import spsolve


def getCoefficientMatrix(indexes):

    nonzero_cnt = len(np.where(indexes != 0)[0].tolist())
    coeffA = np.identity(nonzero_cnt) * 4

    r,c = indexes.shape
    for i in range(r):
        for j in range(c):
            if indexes[i,j] != 0:
                idx = indexes[i,j]

                #check left side of the pixel
                if j-1 > 0:
                    left_idx = indexes[i,j-1]
                    if left_idx > 0:
                        coeffA[idx-1,left_idx-1] = -1

                #check right side of the pixel
                if j < c-1:
                    right_idx = indexes[i,j+1]
                    if right_idx > 0:
                        coeffA[idx-1,right_idx-1] = -1

                #check above of the pixel
                if i-1 > 0:
                    up_idx = indexes[i-1,j]
                    if up_idx > 0:
                        coeffA[idx-1,up_idx-1] = -1

                #check above of the pixel
                if i < r- 1:
                    down_idx = indexes[i+1,j]
                    if down_idx > 0:
                        coeffA[idx-1,down_idx-1] = -1


    return coeffA
