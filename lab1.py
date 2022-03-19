import math

# 1
a = 5
b = 3
c = 4.5
d = 2.43
e = "napis"
f = 'alamakota'
g = 3 + 2j
h = 5 + 6j

print(a, b, c, d, e, f, g, h)

# 2
a = 6
b = 3
print(a+b, a-b, a*b, a/b)

# 3
a = input("Podaj operator: ")
b, c = 8, 4
print(b, a, c, "=")
if a == '+':
    print(b + c)
elif a == '-':
    print(b - c)
elif a == '*':
    print(b * c)
elif a == '/':
    print(b / c)
elif a == '**':
    print(b ** c)
elif a == '%':
    print(b % c)
else:
    print("Bledny znak")

# 4
print(math.e**10)
print(math.log(5+math.sin(8)**2, math.e)**(1/6))
print(math.floor(3.55))
print(math.ceil(4.8))


# 5
a = "MIŁOSZ"
b = "RUSZCZYŃSKI"

a = a.capitalize()
b = b.capitalize()

print(a, b)

# 6
a = 'la la la'
b = a.count('la')
print(b)

# 7
a = 'Miłosz'
print(a[1], a[-1])

# 8
a = 'la la la'
b = a.split()
print(b)

# 9
a = "alamakota"
b = 4.6
c = 0x5345
print(type(a), type(b), type(c))