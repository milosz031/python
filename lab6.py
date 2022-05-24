import numpy as np


# 1
a1 = np.arange(20)*4
print(a1)


# 2
b1 = np.array([0.2, 1.6, 4.1])
print(b1)
b2 = b1.astype('int32')
print(b2)


# 3
def p2(n):
    c1 = 2**np.arange(n*n)
    c1 = c1.reshape(n, n)
    return c1

print(p2(3))


# 4
def pl(p, l):
    d1 = np.logspace(1, l, num=l, base=p, dtype='int32')
    return d1

print(pl(2, 7))


# 5

def f5(d):
    e1 = np.arange(d)+1
    e2 = e1[::-1]
    e3 = np.diag(e1, 2)
    print(e1, e2, '\n',e3)

f5(3)


# 6

f1 = np.array([['a', 'l', 'k', 'a'], ['-', 'r', '-', '-'], ['-', '-', 'k', '-'], ['a', 'i', 'n', 'a']])
print(f1)

# 7
def w2(n):
    a = (np.arange(n * n) + 1).reshape(n, n)
    b = np.arange(n) * (n + 1)
    b = np.diag(b)
    a = a - b

    a[-1] = a[0, ::-1]
    a[:, 0] = a[0]
    a[:, -1] = a[0, ::-1]

    return a

print(w2(4))







