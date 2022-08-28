import math
import numpy as np
import random
import pandas as pd
import math


def copy_values(X, X_hat):
    n, m = X.shape
    for i in range(n):
        for j in range(m):
            if not math.isnan(X[i][j]):
                X_hat[i][j] = X[i][j]
    return X_hat


def map_to_rating_values(X):
    n, m = X.shape
    for i in range(n):
        for j in range(m):
            val = X[i][j]
            if val <= 1.5:
                X[i][j] = 1
            elif 1.5 < val <= 2.5:
                X[i][j] = 2
            elif 2.5 < val <= 3.5:
                X[i][j] = 3
            elif 3.5 < val <= 4.5:
                X[i][j] = 4
            else:
                X[i][j] = 5

    return X

def mat2df(X):
    # 读取矩阵 转化为dataframe 三列 row col ratings

    row_Id = []
    col_Id = []
    ratings = []
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if not math.isnan(X[i][j]):
                row_Id.append(i)
                col_Id.append(j)
                ratings.append(X[i][j])
    data = {
        'row':row_Id,
        'col':col_Id,
        'ratings':ratings
            }
    new_data = pd.DataFrame(data)
    return new_data