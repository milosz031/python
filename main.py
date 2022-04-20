import numpy as np
import pandas as pd


s = pd.Series([1, 3 ,5.5, np.nan, 'a'])
# print(s)

s1 = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s1)

dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(dane)
# print(df)
#
# daty = pd.date_range('20220420', periods=5)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)
#
# df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# print(df)
# df.to_csv('nowy.csv', index=False)
#
# xlsx = pd.ExcelFile('1.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('nowy.xlsx', sheet_name='Arkusz1', index=False)

print(s1['a'])
print(s1.a)

print(df['Populacja'])

print('kraj: '+df.Kraj)

print(df.iloc[[0]])

print(df.head(1))

print(df.tail(1))

print(s1[s1 > 10])
print(s1.where(s1 > 10, 'element nie spelnia warunku'))
seria = s1.copy()
seria.where(seria > 10, 'element nie spelnia warunku', inplace=True)
print(seria)

print(s1[~(s1 > 10)])
print(s1[(s1 < 13) & (s1 > 8)])

print(df[df['Populacja'] > 1200000000])
print(df[((df.Populacja > 1000000) & (df.index.isin([0, 2])))])

szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))

s1['e'] = 15
print(s1)

df.loc[3] = 'nowy element'
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)

df.drop(3, inplace=True)
print(df)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

print(df.sort_values(by='Kraj'))

grupa = df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))
print(df.groupby('Kontynent').agg({'Populacja': ['sum']}))