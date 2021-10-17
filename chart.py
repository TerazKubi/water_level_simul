import numpy as np
import matplotlib.pyplot as plt
from math import sqrt



def h2(n1):
    A = 2
    BET = 0.035
    TP = 0.1
    QD = 0.05

    n = int(n1/TP)
    t = []

    for x in range(0, n):
        if x == 0:
            t.append(0)
        else:
            t.append((1/A) * (-1 * BET * sqrt(t[x-1]) + QD) * TP + t[x-1])

    y = t
    x_ = [i for i in range(0, len(y))]
    plt.plot(x_, y)
    plt.ylabel('Wysokość [m]')
    plt.xlabel('Okres próbkowania')
    plt.title("Symulacja zbiornika,   podany czas:"+str(n1)+" [s].")
    plt.savefig('static/img_folder/test.png', dpi=72)
    plt.close()

