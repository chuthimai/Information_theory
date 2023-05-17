import numpy as np
import math
import random as rd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def Entropy(p, q, r):
    return -(p*math.log2(p) + q*math.log2(q) + r*math.log2(r))


def draw_pqH():
    p = []
    q = []
    r = []
    H = []

    for i in range(0, 3000):
        a = rd.random()
        p.append(a)
        b = 1
        while b > 1 - a:
            b = rd.random()
        q.append(b)
        r.append(1 - a - b)
        entropy = Entropy(a, b, 1 - a - b)
        H.append(entropy)

    fig1 = plt.figure("Đồ thị tập giá trị của H(X) theo p và q")
    ax1 = plt.axes(projection="3d")
    p = np.array(p)
    q = np.array(q)
    H = np.array(H)
    ax1.scatter3D(p, q, H, c=H, cmap=plt.get_cmap("gist_rainbow_r"))
    ax1.set_xlabel("p")
    ax1.set_ylabel("q")
    ax1.set_zlabel("H(X)")


def Hp0_max(p0):
    p = 1
    H = []
    for i in range(0, 100):
        while p > 1-p0:
            p = rd.random()
        q = 1-p0-p
        entropy = Entropy(p, q, p0)
        H.append(entropy)
    return max(H)


def draw_Hp0_max():
    p0 = [rd.random() for i in range(0, 3000)]
    fig = plt.figure("Đồ thị tập giá trị Hp0_max theo p0")
    Hp0 = np.array([Hp0_max(p) for p in p0])
    p0 = np.array(p0)
    plt.scatter(p0, Hp0, c=Hp0, cmap=plt.get_cmap("jet"), marker=".")
    plt.xlabel("p0")
    plt.ylabel("Hp0")


draw_Hp0_max()
draw_pqH()

plt.show()


