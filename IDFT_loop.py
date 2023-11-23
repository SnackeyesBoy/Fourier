import numpy as np

def IDFT_loop(X):

    N = len(X)
    x = []
    
    for n in range(N):
        x_n = 0
        for k in range(N):
            x_n += X[k] * np.exp(2j * np.pi * k * n / N)
        x.append(x_n / N)  # 此處進行標準化
    
    return x



X = [10, -3+1j, 0, -3-1j]
# 計算 IDFT
result = IDFT_loop(X)
print("IDFT_loop_result：", result)
