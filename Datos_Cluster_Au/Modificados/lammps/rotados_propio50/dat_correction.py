import os
import shutil
import subprocess
import numpy as np

def cmd(commando):
    subprocess.run(commando, shell=True)

path = 'C:\\Users\\sergi\\Documents\\Materials Studio Projects\\VERANO2022_Files\\Provericyt_Verano_2022\\Datos_Cluster_Au\\Modificados\\lammps\\rotados_propio50'

carpetas = np.delete(os.listdir(path), (os.listdir(path).index('runner.py')) )

for carpeta in carpetas:
    files = os.listdir(path + '\\' + carpeta)
    for file in files:
        lmp = path + '\\' + carpeta + '\\' + file + '\\in.lmp'
        dat = path + '\\' + carpeta + '\\' + file 
        py = path + '\\' + carpeta + '\\' + file + '\\stress_strain.py'
        dir_py = path + '\\' + carpeta + '\\' + file + '\\' + file
        
        with open(lmp, 'r') as file :
            filedata = file.read()
        filedata_1 = filedata_1.replace('gaussian.dat', '"'+dat+'"')
        with open(lmp, 'w') as file:
            file.write(filedata_1)

        with open(py, 'r') as file :
            filedata_2 = file.read()
        filedata_2 = filedata_2.replace('"/home/mejia/Documents/PROVERICYT/simulacion_9"', '"'+dat+'"')
        with open(py, 'w') as file:
            file.write(filedata_2)
