'''Пусть горка имеет форму, которую можно описать формулами
cos(x)
cos(x) + 0.1*x2
-tanh(x-π/2)
-0.2*(x- π)3 + 0.5*(x- π)2 +1
На отрезке от 0 до π.
Найти длину этих горок.
'''

import matplotlib.pyplot as plt
import numpy as np

eps = 0.0001
x = np.array([i*eps for i in range(0, 31400)])



def f_1(x):
    return np.cos(x)

def f_2(x):
    return np.cos(x) + 0.1 * (x ** 2)

def f_3(x):
    return -np.tanh(x - np.pi / 2)

def f_4(x):
    return -0.2 * (x - np.pi) ** 3 + 0.5 * (x - np.pi) ** 2 + 1



def s(x, f, eps):
    line=0
    for i in range(len(x)-1):
        a=f(x[i])
        b = f(x[i+1])
        del_len = (eps**2 + abs(a-b)**2)**0.5
        line+=del_len
    return line


f = f_2

# Ищем решения
answer = round(s(x, f, eps), 5)
print(answer)


plt.plot(x, f(x))
plt.axhline(color='black')
plt.axvline(color='black')
plt.grid(True)
plt.show()
