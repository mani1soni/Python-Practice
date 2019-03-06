#!/usr/bin/env-python3
'''
required module - numpy
pip3 install numpy #for python3
input = a b
'''
import numpy as np
n,m = map(int, input().split())
arr = np.array([input().strip().split() for _ in range(n)], int)
print(np.transpose(arr))
print(arr.flatten())
