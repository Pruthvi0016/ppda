import numpy as np
matrix1 = np.random.randint(1, 11, (3, 3))
matrix2 = np.random.randint(1, 11, (3, 3))
subtraction_result = matrix1 - matrix2
division_result = np.divide(matrix1, matrix2, where=matrix2!=0)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Subtraction Result:")
print(subtraction_result)

print("\nElement-wise Division Result:")
print(division_result)
