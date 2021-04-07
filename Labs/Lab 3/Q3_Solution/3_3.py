#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:44:48 2021

@author: user
"""

import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt

def show(x,cmap='gray'):
    plt.imshow(x)
    plt.show()

img = cv2.imread("q34.png")

show(img)

fimg = img.reshape(-1, img.shape[2])

fimg = fimg//10

unique,counts =np.unique(fimg, return_counts=True, axis=1)

ind = np.argsort(counts)

unique = unique[ind]

counts = counts[ind]

test = np.where(np.isin(fimg,unique[-1:]),np.ones(fimg.shape),np.zeros(fimg.shape))

test = test.reshape(img.shape)

show(test)