import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)


# 1

# grupa = df.groupby('Rok').agg({'Liczba':['sum']})
# w1 = grupa.plot()
# w1.set_xlabel('Rok')
# w1.set_ylabel('Liczba')
# w1.set_title('Liczba dzieci urodzonych w danym roku')
# plt.legend()
# plt.show()


# 2

# grupa = df.groupby('Plec').agg({'Liczba':['sum']})
# print(grupa)
# w2 = grupa.plot.bar()
# w2.set_xlabel('Plec')
# w2.set_ylabel('Liczba urodzeń')
# w2.set_title('Ogólna liczba urodzeń 2000-2017')
# plt.legend()
# plt.show()


# 3

# g = df[(df.Rok) > 2012]
# print(g)
# grupa = g.groupby(['Rok', 'Plec']).agg({'Liczba':['sum']})
# print(grupa)
#
# w3 = grupa.plot(kind='pie', subplots=True, autopct= '% .2f %%', fontsize=13, figsize=(6,6), legend=(0, 0))
#
# plt.title('Ilość urodzeń 2013-2017')
# plt.show()


# 4

# df = pd.read_csv('datasets/zamowienia.csv', sep=';')
# print(df)
#
# grupa = df.groupby('Sprzedawca').agg({'Sprzedawca':['count']})
# print(grupa)
# w4 = grupa.plot.bar(fontsize=6)
# w4.set_xlabel('Sprzedawca')
# w4.set_ylabel('Ilość zamówienie')
# w4.set_title('Ilość zamówień poszczególnych sprzedawców')
# plt.legend()
# plt.show()