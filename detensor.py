import numpy as np

from tensor import tensor2_matrix

def detensor2(x2,d):
    # turn vector into matrix
    x2_restore = np.zeros((d,d))
    key = 0
    for i in range(0,d):
        for j in range(i,d):
            x2_restore[i][j] = x2[key]
            key += 1
    for i in range(1,d):
        for j in range(0,i):
            x2_restore[i][j] = x2_restore[j][i]
    
    #detensorization ---use max eigenvalue&vector
    lam,vec = np.linalg.eig(x2_restore)
    x = np.abs(np.sqrt(np.abs(lam[0]))*vec[:,0])
    return x

def detensor2_matrix(X2,d):
    n = np.shape(X2)[0]
    T = tuple(detensor2(X2[i,:],d) for i in range(0,n))
    X = np.row_stack(T)

    return X