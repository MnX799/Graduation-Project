import math

def RMSE(X0,X_hat):
    '''
    compute ||X_hat-X0||_F using nonnan elements in X0
    '''
    n,d = X0.shape
    power_sum = 0
    sum = 0
    for i in range(0,n):
        for j in range(0,d):
            if not math.isnan(X0[i][j]):
                power_sum += (X_hat[i][j]-X0[i][j])*(X_hat[i][j]-X0[i][j])
                sum += 1

    eval = math.sqrt(power_sum/sum)

    return eval