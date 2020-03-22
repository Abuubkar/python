import numpy as np
# or use
# from numpy import array

a = np.array([1, 2, 3, 4])  # RANK 1 ARRAY
# np.array(list , dtype=np.float64)

print("Array: ")
print(a)
# l = [1, 2, 3, 4]
# print("List: ")
# print(l)

# Lists are like array but comma seperated
# print(a*2)
# print(l*2)

# Dimension
print(a.shape)

# Rank 2 array
b = np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]])
print(b)
print(b.shape)
print("from row 1 to end:")
print(b[1:])  # b[start from row : no of coloms]
print("row 1:")
print(b[1, :])  # , tell show this row only

print("all row , column 2:")
print(b[0:3, 1:2])

print("column 2:")
print("rank 1")
print(b[:, 2])
print("rank 2")
print(b[:, 2:])

# Numpy arrays are assignmented as Refference
# b = a[2:]
# means change in b will affect a

# =============================== Boolean Array indexing
print("Boolean array indexing")
c = a > 3
print(a)
print(c)
print(a[a > 3])
print(a[c])
# =============================== Transpose
print("Transpose")
print(a.T)  # rank 1 doesnot affect
print(b.T)
