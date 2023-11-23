import numpy as np

# def IDFT_matrix(N):   
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     F = np.exp(2j * np.pi * k * n / N)/N
#     return F
    
def IDFT_matrix(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(2j * np.pi * k * n / N)/N
    X = np.dot(F, x)
    return X

x = [10, -3+1j, 0, -3-1j]

result = IDFT_matrix(x)
print("IDFT_matrix_result：", result) 