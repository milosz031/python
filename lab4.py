import random

# 1
plik = open("plik.txt", "w+")

a = random.randint(0, 30)*2

plik.write(str(a))

plik.close()

# 2
plik = open("plik.txt", "r")

wiersze = plik.readlines()

print(wiersze)

plik.close()

# 3
with open("plik.txt", "a+") as plik:
    for linia in plik:
        print(linia,end="")
plik.write("tekst")

wiersze2 = plik.read()

print(wiersze2)

plik.close()