#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:41:37 2021

@author: user
"""

import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt

def prominance(unique):
    
    l1 = np.tile(unique[1],(10,10,1))
    l2 = np.tile(unique[2],(10,10,1))
    l3 = np.tile(unique[3],(10,10,1))
    m1 = np.tile(unique[-1],(10,10,1))
    m2 = np.tile(unique[-2],(10,10,1))
    m3 = np.tile(unique[-3],(10,10,1))
    
    fig, axes = plt.subplots(nrows=2, ncols=3)
    axes[0,0].imshow(l1)
    axes[0,1].imshow(l2)
    axes[0,2].imshow(l3)
    axes[1,0].imshow(m1)
    axes[1,1].imshow(m2)
    axes[1,2].imshow(m3)
    fig.tight_layout()
    
def show(x,cmap='gray'):
    plt.imshow(x)
    plt.show()

img = cv2.imread("q34.png")

show(img)

fimg = img.reshape(-1, img.shape[2])

colors = np.array([[0, 0, 0],
            [128, 128, 128],
            [128, 0, 0],
            [0, 255, 0]])

dist = np.array([[ np.linalg.norm(i-j) for j in colors] for i in fimg])

dist = np.linalg.norm(fimg[:, None, ...] - colors[None, ...], axis=-1)

cluster = np.argmin(dist,axis=1)

fimg = colors[cluster]


fimg = fimg//10

fimg = fimg*10

unique,counts =np.unique(fimg, return_counts=True, axis=0)

ind = np.argsort(counts)

unique = unique[ind]

counts = counts[ind]

test = np.where(np.isin(fimg,unique[:1]),np.ones(fimg.shape),np.zeros(fimg.shape))

test = test.reshape(img.shape)

test = np.logical_or(test[:,:,0],test[:,:,1],test[:,:,2])

show(test)

dominant = np.tile(unique[:1],(100,100,1))

show(dominant)