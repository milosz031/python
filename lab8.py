import pandas as pd
import numpy as np

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index =['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
# print(s)
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
#
# daty = pd.date_range('20210324', periods=5)
# print(daty)
#
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)

# 1
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)


# 2
print(df[df['Liczba'] >= 1000])

grupa = df.groupby(['Imie'])
name = (grupa.get_group('MIŁOSZ'))
print(name)

print('')

grupa = df[('Liczba')].sum()
print(grupa)

print('')

r2005 = (df[df['Rok'] < 2005])
grupa  = r2005[('Liczba')].sum()
print(grupa)

print('')

grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
print(grupa)

print('')

grupa = df.groupby(['Imie']).agg({'Liczba': ['sum']})
print(grupa)

print('')


# 3

df = pd.read_csv('datasets/zamowienia.csv', sep=";", decimal=".")
print(df)

grupa = df.groupby('Kraj').agg({'Sprzedawca':['unique']})
print(grupa)

z5 = df.sort_values('Utarg')
print(z5.tail())

print('')

grupa = df.groupby('Sprzedawca').agg({'Utarg':['count']})
print(grupa)

print('')

grupa = df.groupby('Kraj').agg({'Kraj':['count']})
print(grupa)

print('')

r2005 = df[(df.Kraj == 'Polska') & (df.Data_zamowienia >= '2005-01-01')]
g5 = r2005.agg({'Kraj':['count']})
print(g5)

print('')

r2004 = df[(df.Data_zamowienia >= '2004-01-01') & (df.Data_zamowienia <= '2004-12-31')]
g4 = r2004.agg({'Utarg':['mean']})
print(g4)

g5.to_csv('zamowienia_2005.csv', index=False)
g4.to_csv('zamowienia_2004.csv', index=False)



