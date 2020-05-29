'''
  File name: getSolutionVect.py
  Author: Tien Pham
  Date created: 10/1/2019
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
import scipy.sparse.linalg
from scipy.sparse.linalg import spsolve


def getSolutionVect(indexes, source, target, offsetX, offsetY):
    laplacian = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    laplacian_source = signal.convolve2d(source,laplacian,'same')

    #get the location of the source on the target image
    source_row = offsetY + source.shape[0]
    source_col = offsetX + source.shape[1]
    domain_source = indexes[offsetY : source_row, offsetX : source_col]
    SolVectorb = laplacian_source[domain_source != 0]


    neighbor_lst = []
    for i in range(offsetX, source_row):
        for j in range(offsetY,source_col):
            if indexes[i,j] != 0:

                #check the left pixel
                if j - 1 > 0:
                    if indexes[i,j-1] == 0:
                        left = target[i,j-1]
                    else:
                        left = 0

                #check the right pixel:
                if j + 1 < target.shape[0]:
                    if indexes[i,j+1] == 0:
                        right = target[i,j-1]
                    else:
                        right = 0

                 #check the above pixel:
                if i - 1 > 0:
                    if indexes[i-1,j] == 0:
                        up = target[i-1,j]
                    else:
                        up = 0

                 #check the below pixel:
                if i + 1 < target.shape[0]:
                    if indexes[i+1,j] == 0:
                        down = target[i+1,j]
                    else:
                        down = 0

                value = left + right + up + down
                neighbor_lst.append(value)


    neighbor_vector = np.array(neighbor_lst)

    SolVectorb  = SolVectorb + neighbor_vector


    return SolVectorb
