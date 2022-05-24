import numpy as np


# 1

a1 = np.array([6, 1, 5])
a2 = np.arange(3)+1
a3 = a1*a2
print(a3)


# 2

b1 = np.array([[1, 4, 2], [6, 3, 5], [9, 7, 8]])

print(b1)
print(b1.min(axis=0))
print(b1.min(axis=1))


# 3

print(a1.dot(a2))


# 4

c1 = np.arange(3, dtype='int32')
c2 = np.linspace(0.1, 0.3, num=3)
print(c1*c2)


# 5

d1 = np.array([[5, 2, 3], [1, 6, 4]])
a = np.sin(d1)
print(a, '\n')


# 6
e1 = np.array([[5, 2, 3], [1, 6, 4]])
b = np.cos(e1)
print(b, '\n')


# 7

print(a+b)


# 8

f1 = np.random.randint(6, size=[3, 3])

for i in range(3):
    print(f1[i])


# 9

g1 = np.random.randint(6, size=[3, 3])

for b in g1.flat:
    print(b)


# 10

h1 = np.random.randint(81, size=[9, 9])
h1 = h1.reshape(1, 81)
print(h1.shape)
h1 = h1.reshape(27, 3)
print(h1)


# 11

i1 = np.random.randint(12, size=[12])
i1 = i1.ravel()
i2 = i1.reshape(3, 4)
i2 = i2.ravel()
i3 = i1.reshape(4, 3)
i3 = i3.ravel()
i4 = i1.reshape(2, 6)
i4 = i4.ravel()
print(i1, i2, i3, i4)

