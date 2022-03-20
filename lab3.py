import random
from pakiet2.funkcje import *

# 1
a = [1-x for x in range(0, 10)]

print(a)

b = [4**x for x in range(0, 7)]

print(b)

c = [x for x in b if x % 2 == 0]

print(c)

# 2
a1 = []
i = 0

while i<10:
    b = random.randint(0, 100)
    a1.append(b)
    i+=1

a2 = [x for x in a1 if x % 2 == 0]
print(a2)

# 3
slownik = {'jabłka': 'kg', 'woda': 'szt', 'masło': 'szt' }

ts = {x for x,y in slownik.items() if y == 'szt'}

print(ts)

# 4
def ctp(a, b, c):
    if (a**2)+(b**2)==(c**2):
        return "Jest prostokatny"
    else:
        return "Nie jest"


a = int(input("Podaj 1 przyprostokatna: "))
b = int(input("Podaj 2 przyprostokatna: "))
c = int(input("Podaj przeciwprostokatna: "))
print(ctp(a, b, c))

# 5
def pt(a, b, h):
    return ((a+b)*h)/2

print(pt(1, 2, 3))

# 6
def ciag(a, b, ile):
    i = 1
    while i<ile:
        i += 1
        a=a*b
    return a


print(ciag(1, 4, 10))

# 7
def ciag2(*liczby):
    a = 1
    b = 4
    ile = 10
    i = 1
    while i<ile:
        i += 1
        a=a*b
    return a


print(ciag2())

# 8
def lz(**zakupy):
    return len(zakupy)


print(lz(mleko= 4, chleb= 4,))

# 9
a = 1
r = 2
q = 2
n = 5
print(ca(a, r, n))
print(cg(a, q, n))
