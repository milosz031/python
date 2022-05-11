import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# plt.plot([1, 2, 3, 4])
# plt.ylabel('jakies liczby')
# plt.show()


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()


# t = np.arange(0., 5., 0.2)
#
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()


# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x, x**3, label="sześcienna")
#
# plt.xlabel('etykieta x')
# plt.ylabel("etykieta y")
#
# plt.title("Prosty wykres")
#
# plt.legend()
# plt.savefig('wykres matplot.png')
#
# plt.show()
#
# im1 = Image.open('wykres matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')


# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label="sin(x)")
#
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.title('Wykres sin(x)')
#
# plt.legend()
#
# plt.show()


# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d'] * 100)
#
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()


# 1
# x = np.arange(1, 22, 2.5)
# y = 1/x
#
# plt.plot(x, y, 'g--^',  label="f(x) = 1/x")
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.show()


# 3
# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y, label="sin(x)")
# plt.plot(x, y2, label="cos(x)")
# plt.title("Wykres sin(x), cos(x)")
# plt.xlabel('x')
# plt.ylabel('sin(x), cos(x)')
# plt.legend(loc='upper right')
# plt.show()


# 5
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

grupa = df.groupby(by='')