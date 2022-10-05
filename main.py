#2a
i = 1
lista = []
while i<=10:
    lista.append(i)
    i += 1
print(lista)

#2b
i = 0
lista = []
while i<=20:
    lista.append(i)
    i += 2
print(lista)

#2c
i = 1
p = i
lista = []
while i<=10:
    lista.append(p)
    i += 1
    p = i ** 2
print(lista)

#2d
i = 1
p = 0
lista = []
while i<=10:
    lista.append(p)
    i += 1
print(lista)

#2e
i = 1
p = 0
lista = []
while i<=10:
    if i%2==0:
        lista.append(p+1)
    else:
        lista.append(p)
    i += 1
print(lista)

#2f
i = 1
p = 0
lista = []
while i<=10:
    if p>4:
        p = 0
    lista.append(p)
    p += 1
    i += 1
print(lista)

#3
lista = [1, 3, 6, -3 ,2 ,1, -6]

def ile_ujemnych(l):
    suma = 0
    for el in l:
        if el < 0:
            suma += 1
    return suma

print(ile_ujemnych(lista))

def iloczyn(l):
    il = 1
    for el in l:
         il *= el
    return il

print(iloczyn(lista))

def minmax(l):
    maks = float('-inf')
    min = float('inf')
    for el in l:
        if el < min:
            min = el
        elif el > maks:
            maks = el
        mm = [min, maks]
    return mm

print(minmax(lista))

def sp(l):
    suma = 0
    for el in l:
        if el % 2 == 0:
            suma += el
        else:
            suma -= el
    return suma

print(sp(lista))

a = int(input('Podaj liczbe: '))
i = 0

for el in lista:
    if el == a:
        i = 1
        break
if i != 1:
    lista.append(a)
print(lista)

lista = []
i = 2

while i<=10000:
    lista.append(i)
    i += 1

print(lista)


#9a

lista = [1,4,9,16,25]

a = lista[0]
lista[0] = lista[-1]
lista[-1] = a
print(lista)

#9b

lista = [1,4,9,16,25]
a = 0

while a < len(lista):
    b = lista[a]
    lista[a] = lista[a-1]
print(lista)
#10

def equals(a, b):
    if len(a) != len(b):
        return "Inna"