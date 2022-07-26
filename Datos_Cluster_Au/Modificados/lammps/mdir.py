import os
import shutil

carpetas =  [
             'random',
             'gaussiana',
             'lineal',
             'cuadratica', 
             'step',
             'sigmoide',
             'tan_hiper'
]

for carpeta in carpetas:
    for i in range(0, 365, 5):
        dir = "rotados_PtNi/" + carpeta + '/' + str(i)
        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print("Directory already existed : ", dir)
        shutil.copy("in.lmp", "rotados_propio50/" + carpeta + '/' + str(i) + '/' + 'in.lmp')