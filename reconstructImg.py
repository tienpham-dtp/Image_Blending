'''
  File name: reconstructImg.py
  Author:
  Date created:
'''

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
import scipy.sparse.linalg
from scipy.sparse.linalg import spsolve


def reconstructImg(indexes, red, green, blue, targetImg):
    #create an empty matrix with targetImg shape
    resultImg = targetImg.copy()

    resultImg[:,:,0][np.where(indexes!=0)] = red
    resultImg[:,:,1][np.where(indexes!=0)] = green
    resultImg[:,:,2][np.where(indexes!=0)] = blue
    resultImg = resultImg.astype('uint8')

    return resultImg
