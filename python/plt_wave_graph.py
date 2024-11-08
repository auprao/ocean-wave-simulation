import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from mpl_toolkits import mplot3d

af = 0.3 # angular frequency (time)
k = 0.8 # wave number (stretch)
span = 4 # axes limits (graph)
min_span, max_span  = -span, span

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

def sinus(x, y, t) :
    return np.sin(k*x + k*y + af*t) 

def wave2(x, y, t) :
    return np.sin(k*x + k*y + af*t) * np.sin(k*x + af*t) * np.sin(k*y + af*t) 

writer = PillowWriter(fps=10)

xlist, ylist = np.meshgrid(np.linspace(min_span, max_span, 201), np.linspace(min_span, max_span, 201))
zlist = []


with writer.saving(fig, ".\python\sin_wave.gif", 200) :
    for t in np.linspace(0, 10, 51) :
        zlist = sinus(xlist, ylist, t)

        ax.contour(xlist, ylist, zlist, zdir='z', offset=-100, cmap='coolwarm')

        ax.set(xlim=(min_span, max_span), ylim = (min_span, max_span), zlim=(-5, 5), xlabel="x", ylabel="y", zlabel="z")

        #ax.plot_surface(xlist, ylist, zlist, cmap="Blues_r")
        ax.plot_surface(xlist, ylist, zlist)

        writer.grab_frame()

        plt.cla()

