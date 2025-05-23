import numpy as np

A = np.array([[2, 4],
              [1, 3]])

B = np.array([[5, 7],
              [6, 8]])

result = np.matmul(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Multiplication Result:\n", result)
