import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def simulate(time, wanted_height, kp, ti, td, a, qdmax, umax):
    #STALE
    KP = float(kp)
    TI = float(ti)
    TD = float(td)

    A = int(a)
    BET = 0.035
    TP = 0.1

    QD_max = float(qdmax)
    U_max = int(umax)


    wanted_height = float(wanted_height)
    n = int(time / TP)
    h = []

    # tablica pomocnicza to obliczania sumy
    e_tab = []
    e_sum = 0
    u_tab = []

    for x in range(0, n):
        if x == 0:
            h.append(x)
            e = wanted_height - h[x]
            e_tab.append(e)
            e_sum += e
            u_tab.append(x)
        else:
            # obliczenie E ===============================
            e = wanted_height - h[x - 1]
            # dodanie e do e_tab by pomoc w obliczeniu U
            e_tab.append(e)
            e_sum += e
            # ============================================
            # obliczenie U ===============================
            u = KP * (e_tab[x] + ((TP / TI) * e_sum) + ((TD / TP) * (e_tab[x] - e_tab[x - 1])))
            u_tab.append(u)
            # ============================================
            # obliczenie QD ==============================
            qd = (QD_max / U_max) * u
            # ============================================
            h.append((1 / A) * (-1 * BET * sqrt(h[x - 1]) + qd) * TP + h[x - 1])

    y = h
    x_ = [i for i in range(0, len(y))]
    plt.plot(x_, y)
    y2 = [wanted_height] * len(y)
    plt.plot(x_, y2)
    # plt.plot(x_, u_tab)
    plt.ylabel('Wysokość [m]')
    plt.xlabel('Okres próbkowania')
    plt.title("Symulacja zbiornika,   podany czas:" + str(time) + " [s].")

    plt.legend(["Aktualny poziom", "Zamierzony poziom"])
    #plt.show()
    plt.savefig('static/img_folder/test.png', dpi=72)
    plt.close()
