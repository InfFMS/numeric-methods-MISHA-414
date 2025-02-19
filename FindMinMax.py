import matplotlib.pyplot as plt
import numpy as np


eps=0.001

x1=np.array([i/1000 for i in range(0, 3140)])
def blob1(x):
    return np.sin(2*x)+1, -0.2*x**2 + 0.5   # up, down

x2=np.array([i/1000 for i in range(-2000, 2000)])
def blob2(x):
    return np.exp(-(x**2)) + 1, -0.3*x**3 + 0.5   # up, down
x3=np.array([i/1000 for i in range(-2000, 2000)])
def blob3(x):
    return np.exp(-(x**2)) + 0.5, 0.2*np.sin(3*x)-0.5   # up, down
x4=np.array([i/1000 for i in range(1571, 1571)])
def blob4(x):
    return np.cos(x)+1.2, -0.5*x**2 + 0.7   # up, down
x5=np.array([i/1000 for i in range(-2000, 2000)])
def blob5(x):
    return np.exp(-(x+1)**2) +np.exp(-(x-1)**2) +0.5, -0.3*x**2   # up, down


def area_blob(x, left, right, f, eps):
    fig, ax = plt.subplots()
    y=f(x)

    ax.plot(x, y[0])
    ax.plot(x, y[1])

    x0 = left
    square = 0

    while x0 < right:
        vale_x0=f(x0)
        vale_x0_eps=f(x0+eps)

        average_value_up = (vale_x0[0] + vale_x0_eps[0]) / 2
        average_value_down = (vale_x0[1] + vale_x0_eps[1]) / 2

        # Прямоугольник
        rect = plt.Rectangle((x0 + eps / 2, average_value_down), eps, average_value_up-average_value_down, color="red")
        ax.add_patch(rect)

        del_area = (average_value_up-average_value_down) * eps
        square += del_area
        x0 += eps

    print(square)
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True)
    plt.show()
    return square



area_blob(x5, x5[0], x5[-1], blob5, eps)
