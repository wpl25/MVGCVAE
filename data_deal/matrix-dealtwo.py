# -*- coding: utf-8 -*-

import numpy as np

# Load the first CSV file and convert it to a matrix (e.g., disease cosine similarity)
data1 = np.genfromtxt('TBD', delimiter=',')
matrix1 = np.matrix(data1)

# Load the second CSV file and convert it to a matrix (e.g., disease GIP similarity)
data2 = np.genfromtxt('TBD', delimiter=',')
matrix2 = np.matrix(data2)

# If GIP similarity is non-zero, average the two similarities; otherwise, use only cosine similarity
condition = data2 != 0
result = np.where(condition, (data1 + data2) / 2, data1)

# Save the combined microbe-disease similarity matrix
np.savetxt('TBD', result, delimiter=',')
