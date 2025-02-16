import matplotlib.pyplot as plt
import numpy as np


x=np.array([i/100000 for i in range(0, 1000000)])
eps=0.00001
def f_1(x):
    return (x+1)**0.25 - 2*(x**0.25) - (81*x-1)**0.25

def search_solution(a, b, f, eps):
    while abs(a-b)>eps:
        mid=(a+b)/2
        if f(mid)*f(a)<=0:
            b=mid
        else:
            a=mid
    return a

f=f_1

answer=round(search_solution(0, 10, f, eps), 10)
print(answer)
plt.scatter([answer], [0], color='red')


plt.plot(x, f(x))
plt.axhline(color='black')
plt.axvline(color='black')
plt.grid(True)
plt.show()