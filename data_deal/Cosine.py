import numpy as np
import pandas as pd


# Cosine-based functional similarity
association = pd.read_csv("TBD", header=None).to_numpy()

def Cosine_Sim_row(M):
    l = len(M)
    print(l)
    SM = np.zeros((l, l))
    for i in range(l):
        for j in range(l):
            v1 = np.dot(M[i], M[j])
            v2 = np.linalg.norm(M[i], ord=2)
            v3 = np.linalg.norm(M[j], ord=2)
            if v2 * v3 == 0:
                SM[i][j] = 0
            else:
                SM[i][j] = v1 / (v2 * v3)
    return SM

# Transpose is used to compute similarity between microbes (columns represent microbes)
Cos_Matrix = Cosine_Sim_row(association.T)
print(Cos_Matrix)
print(Cos_Matrix.shape)

df = pd.DataFrame(Cos_Matrix)
# df.to_csv('TBD', index=False, header=False)
# df.to_csv('TBD', index=False, header=False)
