import numpy as np
import math
import random as rd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def Entropy(p, q, r):
    return -(p*math.log2(p) + q*math.log2(q) + r*math.log2(r))


def draw_pqr():
    p = []
    q = []
    r = []
    H = []

    for i in range(0, 1000):
        a = rd.random()
        p.append(a)
        b = 1
        while b > 1 - a:
            b = rd.random()
        q.append(b)
        r.append(1 - a - b)
        entropy = Entropy(a, b, 1 - a - b)
        H.append(entropy)
        # print(f"(p, q, r) = ({a}, {b}, {1-a-b}) => H = {entropy}")

    fig = plt.figure("Đồ thị tập giá trị kết quả theo p, q, r")
    p = np.array(p)
    q = np.array(q)
    r = np.array(r)
    ax = plt.axes(projection="3d")
    ax.scatter3D(q, p, r, c=q, cmap=plt.get_cmap("cool"))
    ax.set_xlabel("p")
    ax.set_ylabel("q")
    ax.set_zlabel("r")


def Hp0_max(p0):
    p = 1
    q = 1
    H = []
    # print(f"Với r = {p0} ta có (p, q, H):")
    for i in range(0, 100):
        while p > 1-p0:
            p = rd.random()
        q = 1-p0-p
        entropy = Entropy(p, q, p0)
        H.append(entropy)
        # print(f"({p}, {q}, {entropy})", end=" ")
    return max(H)


def draw_Hp0_max():
    p0 = [rd.random() for i in range(0, 1000)]
    fig = plt.figure("Đồ thị tập giá trị Hp0_max theo p0")
    Hp0 = np.array([Hp0_max(p) for p in p0])
    p0 = np.array(p0)
    plt.scatter(p0, Hp0, c=p0, cmap="rainbow", marker=".")
    plt.xlabel("p0")
    plt.ylabel("Hp0")


draw_Hp0_max()
draw_pqr()

plt.show()


