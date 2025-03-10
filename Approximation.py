import matplotlib.pyplot as plt
import numpy as np


x=np.array([i/100 for i in range(-1000, 1000)])
eps=0.01

def f_1(x):
    return x**3 - x + 1
def f_2(x):
    return x**3 - x**2 - 9*x + 9
def f_3(x):
    return x**2 - np.exp(x)
def f_4(x):
    return 5*x - 6*np.log(x) - 7
def f_5(x):
    return np.cos(x) + 2*x - 3



def search_solution(a, b, f, eps):
    while abs(a-b)>eps:
        mid=(a+b)/2
        if f(mid)*f(a)<=0:
            b=mid
        else:
            a=mid
    return a

f=f_4

# Ищем решения
answer=round(search_solution(0, 2, f, eps), 10)
print(answer)
plt.scatter([answer], [0], color='red')


plt.plot(x, f(x))
plt.axhline(color='black')
plt.axvline(color='black')
plt.grid(True)
plt.show()

