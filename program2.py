import numpy as np

array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([5, 4, 3, 2, 1])
array_c = np.array([-1.52, 0.57, 2.95, -3.5])

print("Original Array A:", array_a)
print("Original Array B:", array_b)
print("Original Array C:", array_c)

print("\nAddition:", np.add(array_a, array_b))
print("Multiplication:", np.multiply(array_a, array_b))
print("Square Root:", np.sqrt(array_a))
print("Sine:", np.sin(array_a))
print("Absolute Value:", np.abs(array_c))

print("\nSum:", np.sum(array_a))
print("Mean:", np.mean(array_a))
print("Max:", np.max(array_a))
print("Min:", np.min(array_a))
print("Standard Deviation:", np.std(array_a))

rounded_array = np.round(array_c, 1)
print("\nRounded Array C:", rounded_array)
