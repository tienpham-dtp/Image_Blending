'''
  File name: seamlessCloningPoisson.py
  Author: Tien Pham
  Date created: 10/1/2019
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
import scipy.sparse.linalg
from scipy.sparse.linalg import spsolve


def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):

    targetH, targetW, channels = targetImg.shape
    indexes = getIndexes(mask, targetH, targetW, offsetX, offsetY)


    coeffA = getCoefficientMatrix(indexes)
    red_b = getSolutionVect(indexes, sourceImg[:,:,0], targetImg[:,:,0], offsetX, offsetY)
    green_b = getSolutionVect(indexes, sourceImg[:,:,1], targetImg[:,:,1], offsetX, offsetY)
    blue_b = getSolutionVect(indexes, sourceImg[:,:,2], targetImg[:,:,2], offsetX, offsetY)

    r = spsolve(coeffA,red_b)
    g = spsolve(coeffA,green_b)
    b = spsolve(coeffA,blue_b)

    r = np.clip(r,0,255,out = r)
    g = np.clip(g,0,255,out = g)
    b = np.clip(b,0,255,out = b)

    resultImg = reconstructImg(indexes,r ,g ,b ,targetImg)


	return resultImg
