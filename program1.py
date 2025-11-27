import numpy as np

arr = np.arange(12)

print("\n--- Array Creation ---")
print(arr)

print("\n--- Indexing ---")
print(arr[5])

print("\n--- Slicing ---")
print(arr[2:8])
print(arr[:5])
print(arr[6:])
print(arr[::2])

print("\n--- Reshaping ---")
reshaped_arr = arr.reshape(3, 4)
print(reshaped_arr)

print("\n--- Slicing 2D Array ---")
print(reshaped_arr[0, :])
print(reshaped_arr[:, 2])
print(reshaped_arr[0:2, 1:3])

print("\n--- Joining Arrays ---")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
h_join = np.hstack((arr1, arr2))
v_join = np.vstack((arr1, arr2))
print(h_join)
print(v_join)

print("\n--- Splitting Arrays ---")
h_split = np.hsplit(h_join, 2)
v_split = np.vsplit(v_join, 2)
print(h_split)
print(v_split)
