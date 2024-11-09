import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

wave_count = 6
a = 0.2 # amplitude
af = 0.2 # angular frequency (time)
kx = [] # wave number (stretch) for every wave
ky = [] 
for i in range(1, wave_count + 1) :
    kx.append(np.random.rand())
    ky.append(np.random.rand())
    
span = 10 # axes limits (graph)
min_span, max_span  = -span, span

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

def sin_wave(x, y, t) :
    return a * np.sin(kx[0]*x + ky[0]*y + af*t) 

def gerstner_wave(x, y, t) : 
    return sum(a * np.exp(complex(0,1)*(kx[n-1]*x + ky[n-1]*y + np.log(n+1)*af*t + n)).real for n in range(1, wave_count + 1))


writer = PillowWriter(fps=30)

xlist, ylist = np.meshgrid(np.linspace(min_span, max_span, 512), np.linspace(min_span, max_span, 512))
zlist = []


with writer.saving(fig, ".\python\gerstner_wave_4_1.gif", 256) :
    for t in np.linspace(0, 40, 301) :
        zlist = gerstner_wave(xlist, ylist, t)

        ax.contour(xlist, ylist, zlist, zdir='z', offset=-100, cmap='coolwarm')

        ax.set(xlim=(min_span, max_span), ylim = (min_span, max_span), zlim=(min_span, max_span), xlabel="x", ylabel="y", zlabel="z")

        ax.plot_surface(xlist, ylist, zlist, cmap="Blues_r")
        #ax.plot_surface(xlist, ylist, zlist)

        writer.grab_frame()

        plt.cla()

