import numpy as np

# 1
a = np.array([1, 6, 2])
b = np.array([3, 4, 5])
print(a*b)

# 2
c = np.array([[2, 1, 3], [4, 5, 6], [9, 8, 7]])
d = np.arange(16).reshape(4, 4)+1
print(c)
print(d)
for el in c:
    print(min(el))
for el in c.T:
    print(min(el))
print('\n')
for el in d:
    print(min(el))
for el in d.T:
    print(min(el))

# 3
print('\n')
print(a.dot(b))

# 4
e = np.arange(1, 4)
f = np.arange(0.2, 0.7, 0.2)
print(e*f)

# 8
g = np.arange(9).reshape(3, 3)+1
for el in g:
    print(el)
