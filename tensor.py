import numpy as np

def tensor2(x):
    '''
    2 order tensor for a single row x
    input: x,ndarray(d,); output: x2,ndarray(d(d+1)/2,)
    '''
    d = x.shape[0]
    x2 = []
    for i in range(0,d):
        for j in range(i,d):
                x2.append(x[i]*x[j])
    x2 = np.array(x2)
    return x2

def tensor2_matrix(X):
    '''
    2 order tensorized matrix for matrix X, ndarray(n,d(d+1)/2)
    '''
    n = np.shape(X)[0]
    T = tuple(tensor2(X[i,:]) for i in range(0,n))
    X2 = np.row_stack(T)
    return X2            