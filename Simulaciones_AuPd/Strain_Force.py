import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

force = np.loadtxt(r"C:\Users\sergi\Documents\Materials Studio Projects\VERANO2022_Files\Provericyt_Verano_2022\Simulaciones_AuPd\simulacion_5\strain_force.dat", skiprows = 1, usecols = 1)
strain = np.loadtxt(r"C:\Users\sergi\Documents\Materials Studio Projects\VERANO2022_Files\Provericyt_Verano_2022\Simulaciones_AuPd\simulacion_5\strain_force.dat", skiprows = 1, usecols = 0)
plt.scatter(strain, force, c = 'r', s = 0.6)
plt.title('Force vs Strain [eV/Å]')
plt.xlabel('Strain')
plt.ylabel('Force')
plt.savefig(r'C:\Users\sergi\Documents\Materials Studio Projects\VERANO2022_Files\Provericyt_Verano_2022\Simulaciones_AuPd\simulacion_5\graph.png')
plt.clf()