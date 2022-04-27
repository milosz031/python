import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.savefig('wykres.png')
# plt.show()

# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
#
# grupa.plot(kind='bar', ylabel='Populacja', xlabel='Kontynent', rot=0, legend=True, title='Populacja dla kontynentów', color='red')
# plt.legend(loc='upper left')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg(
#         {'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', y='Wartość zamówienia', autopct='%.2f %%', fontsize=20, figsize=(6, 6))
# plt.legend(loc='upper left')
# plt.show()

# df = pd.DataFrame(ts)
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# print(df)
# df.plot()
# plt.legend(['Wartosci', 'Średnia krocząca'])
# plt.show()

# 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
grupa = df.groupby('Rok').agg(
    {'Liczba':['sum']})
grupa.plot(kind='line', ylabel='Liczba', xlabel='Rok', rot=0, legend=True, fontsize=7)
plt.legend()
plt.show()

# 2
# grupa = df.groupby('Plec').agg(
#     {'Liczba': ['sum']})
# grupa.plot