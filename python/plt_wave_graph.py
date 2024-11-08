import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from mpl_toolkits import mplot3d

a = 0.5 # amplitude
af = 0.3 # angular frequency (time)
k = 0.5 # wave number (stretch)
span = 10 # axes limits (graph)
min_span, max_span  = -span, span

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

def sin_wave(x, y, t) :
    return a * np.sin(k*x + k*y + af*t) 

def gerstner_wave(x, y, t) : 
    return a * np.exp(complex(0,1)*(k*x + k*y + af*t))  

writer = PillowWriter(fps=10)

xlist, ylist = np.meshgrid(np.linspace(min_span, max_span, 201), np.linspace(min_span, max_span, 201))
zlist = []


with writer.saving(fig, ".\python\gerstner_wave.gif", 200) :
    for t in np.linspace(0, 10, 51) :
        zlist = gerstner_wave(xlist, ylist, t)

        ax.contour(xlist, ylist, zlist, zdir='z', offset=-100, cmap='coolwarm')

        ax.set(xlim=(min_span, max_span), ylim = (min_span, max_span), zlim=(-5, 5), xlabel="x", ylabel="y", zlabel="z")

        #ax.plot_surface(xlist, ylist, zlist, cmap="Blues_r")
        ax.plot_surface(xlist, ylist, zlist)

        writer.grab_frame()

        plt.cla()

