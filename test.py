import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Zad 1

# nazwy = ['A', 'B', 'C', 'D', 'E']
# wartosci = [35, 45, 12, 40, 39]
# wartosci2 = [-30, -35, -43, -40, -32]
#
# plt.subplot(121)
# plt.barh(nazwy, wartosci, color=['aqua', 'pink', 'orange', 'grey', 'purple'])
# plt.title('Wykres lewy')
# plt.subplot(122)
# plt.barh(nazwy, wartosci2, color=['magenta', 'aqua', 'aqua', 'brown', 'gold'])
# plt.title('Wykres prawy')
# plt.show()

# Zad 2

# xlsx = pd.ExcelFile('ceny2.xlsx')
# df = pd.read_excel(xlsx)
# print(df)
#
# ryz = df[df["Rodzaje towarów"] == "ryż - za 1kg"]
# gryz = ryz.groupby('Rok')
# x1 = list(gryz.groups.keys())
# y1 = gryz.agg({'Wartość':['sum']})
#
# maka = df[df["Rodzaje towarów"] == "mąka pszenna - za 1kg"]
# gmaka = maka.groupby('Rok')
# x2 = list(gryz.groups.keys())
# y2 = gmaka.agg({'Wartość':['sum']})
#
# plt.plot(x1, y1, label='ryź')
# plt.plot(x2, y2, label='mąka')
# plt.title("Wykres")
# plt.xlabel("Rok")
# plt.ylabel("Średnia cena")
# plt.legend()
# plt.text(x=2018, y=1.9, s='INDEKS', size='medium')
# plt.show()


#Zad 3

df = pd.read_csv('nieruchomosci2.csv', header=0, sep=';', decimal=',')
print(df)
df = df.T
print(df)
df = df.reset_index()
print(df)
df.drop(axis=1, columns='index', inplace=True)
df.columns = ['opis', 'metraz', 'rok', 'ilosc']
print(df)



