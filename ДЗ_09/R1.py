import numpy as np

data = np.load("PCA.npy")
U, D, V = np.linalg.svd(data)

for m in range(1, 15):
    D_cuted = np.diag(D[m:])
    if D_cuted.sum()/D.sum() < 0.2:
        print(m)
        break
