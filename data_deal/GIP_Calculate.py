# -*- coding: utf-8 -*-

import numpy as np
import math
import pandas as pd

# Load microbe-disease interaction matrix
A = pd.read_csv('TBD', header=None)
# Add header=None to tell pandas the CSV file has no header row, and the first row is valid data

A_array = A.values
print(A_array.shape)
print(A_array)

def GIP_Calculate(M):  # Calculate Gaussian Interaction Profile (GIP) kernel similarity for microbes
    l = np.size(M, axis=1)  # Get the number of columns (i.e., number of microbes)
    print(l)
    
    sm = []
    m = np.zeros((l, l))
    
    for i in range(l):
        tmp = (np.linalg.norm(M[:, i])) ** 2
        sm.append(tmp)
    
    gamma = l / np.sum(sm)  # Gaussian kernel parameter

    for i in range(l):
        for j in range(l):
            m[i, j] = np.exp(-gamma * (np.linalg.norm(M[:, i] - M[:, j])) ** 2)
    
    return m

Smg = GIP_Calculate(A_array)
print(Smg)
print(Smg.shape)

result = pd.DataFrame(Smg)
result.to_csv('TBD', index=False, header=None)
