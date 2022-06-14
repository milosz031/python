import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from PIL import Image


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
print(df)

plt.savefig('nazwa.png')


