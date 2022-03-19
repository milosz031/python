import math
import sys as system

# # 1
# a = ["piłka nożna", "koszykówka"]
#
# a.reverse()
#
# a.append("hokej")
#
# print(a)
#
# # 2
# slownik = {'zdj': 'zdjęcie', 'pn': 'piłka nożna'}
#
# print(slownik)
#
# # 3
# slownikg = {'lol': 'league of legends', 'cs': 'counter-strike'}
#
# i = 0
#
# for x in slownikg:
#     i += 1
#
# print(slownikg, i)
# i = 0
#
# # 4
# a = input("Podaj zdanie: ")
#
# for x in a:
#     if x == 'a':
#         i += 1
#
# print(i)
#
# # 5
# system.stdout.write("Podaj trzy liczby: ")
# a = int(system.stdin.readline())
# b = int(system.stdin.readline())
# c = int(system.stdin.readline())
#
# wynik = a**b + c
#
# system.stdout.write(str(wynik))
#
# # 6
# a = int(input("Podaj 1 liczbę: "))
# b = int(input("Podaj 2 liczbę: "))
# c = int(input("Podaj 3 liczbę: "))
#
# print(min(a, b, c))
#
# print(max(a, b, c))
#
# # 7
# a = [1, 4, 2.5 ,3,25]
# b = []
#
# for x in a:
#     b.append(x**2)
#
# print(b)
#
# # 8
#
# a = []
# i = 1
#
# while i<=10:
#     i += 1
#     b = int(input("Podaj liczbe: "))
#     if b % 2 == 0:
#         a.append(b)
#
# print(a)

# 9
a = int(input("Podaj liczbe: "))

if a>0:
    print("Blad")
else:
    print(math.sqrt(a))



