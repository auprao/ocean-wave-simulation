import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

def sinus(x, y, t) :
    return np.sin(x + t) * np.sin(y + t)

writer = PillowWriter(fps=10)

xlist, ylist = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
zlist = []



with writer.saving(fig, "sin_wave.gif", 200) :
    for t in np.linspace(0, 10, 51) :
        zlist = sinus(xlist, ylist, t)

        ax.contour(xlist, ylist, zlist, zdir='z', offset=-100, cmap='coolwarm')

        ax.set(xlim=(-5, 5), ylim = (-5, 5), zlim=(-5, 5), xlabel="x", ylabel="y", zlabel="z")

        #ax.scatter(xlist, ylist, zlist)
        ax.plot_surface(xlist, ylist, zlist, cmap="Blues_r")

        writer.grab_frame()

        plt.cla()

