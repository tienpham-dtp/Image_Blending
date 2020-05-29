'''
  File name: getIndexes.py
  Author: Tien Pham
  Date created: 10/1/2019
'''

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
import scipy.sparse.linalg
from scipy.sparse.linalg import spsolve


def getIndexes(mask, targetH, targetW, offsetX, offsetY):
    mask_cp = np.zeros(mask.shape)

    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i,j] != 0:
                mask_cp[i,j] = 1


    end_col = offsetX + mask.shape[1]
    end_row = offsetY + mask.shape[0]

    indexes = np.zeros((targetH,targetW))
    newMask = mask_cp.copy()

    count = 0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask_cp[i,j] != 0:
                count += 1
                newMask[i,j] = count

    indexes[offsetY : end_row, offsetX : end_col] = newMask
    indexes = indexes.astype(int)

	return indexes
