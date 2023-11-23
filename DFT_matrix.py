import numpy as np

# def DFT_matrix(N):  # 創建 N x N 的傅立葉矩陣
    
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     F = np.exp(-2j * np.pi * k * n / N)
#     return F
    
# def DFT(x):
#     N = len(x)
#     F = DFT_matrix(N)
#     X = np.dot(F, x)
#     return X


def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(F, x)
    return X

x = np.array([0, 1, 2, 3])

result = DFT(x)
print("DFT_matrix_result：", result) 