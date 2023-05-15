import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def Griesmer_limit(k, d):
    res = 0
    for i in range(0, k):
        res += math.ceil(d / (2**i))
    return res


def Plotkin_limit(n, k):
    return math.floor((n * 2**(k-1)) / (2**k - 1))


def Hamming_limit(n, t):
    res = 0
    for i in range(0, t+1):
        res = res + math.comb(n, i)
    res = n - math.log2(res)
    return math.floor(res)


def cal_t(d):
    return math.floor((d-1)/2)


# Đồ thị giới hạn Griesmer
k0 = []
d0 = []
Griesmer = []

fig0 = plt.figure("Đồ thị giới hạn Griesmer")
ax0 = plt.axes(projection="3d")
for i in range(0, 16):
    for j in range(0, i+1):
        k0.append(i)
        d0.append(j)
        Griesmer.append(Griesmer_limit(i, j))
k0 = np.array(k0)
d0 = np.array(d0)
Griesmer = np.array(Griesmer)

ax0.scatter3D(k0, d0, Griesmer, c=k0+d0+Griesmer, cmap=plt.get_cmap("cool"))
ax0.set_xlabel("k")
ax0.set_ylabel("d")
ax0.set_zlabel("Griesmer limit")

# Đồ thị giới hạn Plotkin
k1 = []
n1 = []
Plotkin = []

fig1 = plt.figure("Đồ thị giới hạn Plotkin")
ax1 = plt.axes(projection="3d")
for i in range(1, 16):
    for j in range(i, 16):
        k1.append(i)
        n1.append(j)
        Plotkin.append(Plotkin_limit(j, i))
n1 = np.array(n1)
k1 = np.array(k1)
Plotkin = np.array(Plotkin)

ax1.scatter3D(n1, k1, Plotkin, c=n1+k1+Plotkin, cmap=plt.get_cmap("autumn"))
ax1.set_xlabel("n")
ax1.set_ylabel("k")
ax1.set_zlabel("Plotkin limit")

# Đồ thị giới hạn Hamming
n2 = []
t2 = []
Hamming = []

fig2 = plt.figure("Đồ thị giới hạn Hamming")
ax2 = plt.axes(projection="3d")
for i in range(1, 16):
    for j in range(1, i+1):
        n2.append(i)
        t2.append(cal_t(j))
        Hamming.append(Hamming_limit(i, cal_t(j)))
n2 = np.array(n2)
t2 = np.array(t2)
Hamming = np.array(Hamming)

ax2.scatter3D(n2, t2, Hamming, c=n2+t2+Hamming, cmap="winter")
ax2.set_xlabel("n")
ax2.set_ylabel("t")
ax2.set_zlabel("Hamming limit")

plt.show()





