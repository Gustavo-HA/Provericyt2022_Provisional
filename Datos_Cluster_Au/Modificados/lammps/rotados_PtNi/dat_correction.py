import os
import shutil
import subprocess
import numpy as np

def cmd(commando):
    subprocess.run(commando, shell=True)

path = 'C:\\Users\\sergi\\Documents\\Materials Studio Projects\\VERANO2022_Files\\Provericyt_Verano_2022\\Datos_Cluster_Au\\Modificados\\lammps\\rotados_PtNi'

carpetas = np.delete(os.listdir(path), (os.listdir(path).index('dat_correction.py')) )

for carpeta in carpetas:
    files = os.listdir(path + '\\' + carpeta)
    for file in files:
        lmp = path + '\\' + carpeta + '\\' + file + '\\in.lmp'
        dat = path + '\\' + carpeta + '\\' + file + '\\' + file + '.dat'
        
        with open(lmp, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('gaussian.dat', '"'+dat+'"')

        # Write the file out again
        with open(lmp, 'w') as file:
            file.write(filedata)



"""
        with open(lmp, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('gaussian.dat', dat)

        # Write the file out again
        with open(lmp, 'w') as file:
            file.write(filedata)
"""