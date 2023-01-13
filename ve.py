import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm



def yen_ngua():
    x1 = np.linspace(start=-5, stop=7, num=1000)
    y1 = np.linspace(start=-5, stop=5, num=1000)
    x, y = np.meshgrid(x1, y1)
    z = (x / 3) ** 2 - (y / 2) ** 2
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.RdBu, linewidth=0, edgecolor='c', antialiased=False)

    ax.set_zlim(-6, 6)

    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)

    plt.show()


def ve_nhieu_do_thi():
    x = np.linspace(start=-10.0, stop=10.0, num=10)
    y1 = x ** 4 - 2 * x ** 2 - 3
    y2 = 4 * x ** 3 - 4 * x
    y3 = 12 * x ** 2 - 4
    y4 = 24 * x
    fig, ax1 = plt.subplots()

    ax1.plot(x, y1, 'o-', label=r'$y=x^{4}+2x^{2}-3$')
    ax1.plot(x, y2, ':_', label=r"$y'=4x^{3} -4x$")
    ax1.plot(x, y3, '*-', label=r"$y' '=12x^{2} -4$")
    ax1.plot(x, y4, label=r"$y' ' '=24x$")
    ax1.set_xlabel("Trục hoành - x")
    ax1.set_ylabel("Trục tung - y")

    ax1.legend()

    plt.show()




def hyperbol_1_tang():
    x = np.linspace(-9, 9, num=2000)
    y = np.linspace(-9, 9, num=2000)
    x, y = np.meshgrid(x, y)

    z1 = 2 * ((x / 3) ** 2 + (y / 5) ** 2 - 1) ** (1 / 2)
    z2 = -2 * ((x / 3) ** 2 + (y / 5) ** 2 - 1) ** (1 / 2)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    rosen_surf1 = ax.plot_surface(x, y, z1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    rosen_surf2 = ax.plot_surface(x, y, z2, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    fig.colorbar(rosen_surf1, shrink=0.5, aspect=5)
    fig.colorbar(rosen_surf2, shrink=0.5, aspect=5)

    plt.show()


def mat_cau():
    x = np.linspace(-4, 0, num=4000)
    y = np.linspace(-1, 3, num=4000)
    x, y = np.meshgrid(x, y)
    z1 = 4 + (-(x + 2) ** 2 - (y - 1) ** 2 + 4) ** (1 / 2)
    z2 = 4 - (-(x + 2) ** 2 - (y - 1) ** 2 + 4) ** (1 / 2)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf1 = ax.plot_surface(x, y, z1, cmap=cm.Blues, linewidth=0, antialiased=False)
    rosen_surf2 = ax.plot_surface(x, y, z2, cmap=cm.Blues, linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf1, shrink=0.5, aspect=5)
    fig.colorbar(rosen_surf2, shrink=0.5, aspect=5)
    plt.show()
def main():
    ve_nhieu_do_thi()
    yen_ngua()
    hyperbol_1_tang()
    mat_cau()
if __name__ =="__main__":
    main()