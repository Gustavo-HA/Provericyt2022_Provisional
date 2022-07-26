from importlib.resources import path
import numpy as np
import matplotlib.pyplot as plt

path = "/home/mejia/Documents/PROVERICYT/simulacion_9"
dat = path + "/strain_force.dat"
out_dir = path + "/graph.png"

force = np.loadtxt(dat, skiprows = 1, usecols = 1)
strain = np.loadtxt(dat, skiprows = 1, usecols = 0)
plt.plot(strain, force, c = 'r') ### MODIFICAR LAS RUTAS
plt.title('Force vs Strain [eV/Å]')
plt.xlabel('Strain')
plt.ylabel('Force')
plt.savefig(out_dir)
plt.clf()

