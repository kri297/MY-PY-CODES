import numpy as np

arr = np.array([[5, 8, 3],
                [6, 2, 9],
                [1, 7, 4]])

row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)
second_max = np.sort(arr.flatten())[-2]

print("Array:\n", arr)
print("Row-wise sum:", row_sum)
print("Column-wise sum:", col_sum)
print("Second maximum element:", second_max)
