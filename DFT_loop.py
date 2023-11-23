import numpy as np
#import matplotlib.pyplot as plt
#from scipy.ndimage import shift


#DFT-迴圈計算
def DFT_loop(x,N):
    #N = len(x)
    X = []
    
    for k in range(N):
        X_k = 0
        for n in range(N):
            X_k += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(X_k)
        

    return X

x = [0, 1, 2, 3]
N = len(x)
# 計算 DFT
result = DFT_loop(x,N)
print("DFT_loop_result：", result)
print(type(result))