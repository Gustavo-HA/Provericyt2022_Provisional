import os
import shutil

carpetas = [    "lineal",
                "cuadratica",
                "gaussiana",
                "random",
                "sigmoide",
                "step",
                "tan_hiper" ]

for carpeta in carpetas:
    for i in range(0, 365, 5):
        dir = "rotados_old/" + carpeta + '/' + str(i)
        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print("Directory already existed : ", dir)
        shutil.copy( "rotados_old/" + carpeta + '/' + str(i) + '.dat' , "rotados_PtNi/" + carpeta + '/' + str(i) + '/' + str(i) + '.dat' )