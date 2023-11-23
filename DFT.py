import numpy as np

# 示例用法
# 創建一個示例輸入信號
x = np.array([0, 1, 2, 3])
# 計算 DFT
result = np.fft.fft(x)
print("DFT_result：", result)