# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:49:31 2018

@author: congpeiqing
"""
import numpy as np

#sigmoid函数的导数为  f(x)*(1-f(x))
def sigmoid(x) :
    return 1/(1 + np.exp(-x))