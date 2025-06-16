# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import torch as t

# This code implements the HIP (Hamming distance-based Integrated similarity Profile)
# method, which calculates similarity between rows. HIP measures similarity by 
# computing the Hamming distance between binary-encoded samples.
# Specifically, HIP compares each bit in the binary sequence of two samples, and 
# counts the number of differing bits. The similarity is then calculated as 
# 1 - (Hamming distance / total bits).

# Load CSV file and convert to appropriate input matrix
data = pd.read_csv('TBD', header=None)
y = t.tensor(data.values)

def HIP_Calculate(M):
    l = len(M)
    cl = np.size(M, axis=1)
    SM = np.zeros((l, l))
    for i in range(l):
        for j in range(l):
            drum = 0
            for k in range(cl):
                if M[i][k] != M[j][k]:
                    drum += 1
            SM[i][j] = 1 - drum / cl  # HIP similarity matrix
    return SM

# Transpose to compute similarity between microbes
t = HIP_Calculate(y.T)
print(t.shape)
result = pd.DataFrame(t)

result.to_csv('TBD', index=False, header=False)
