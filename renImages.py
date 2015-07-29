import os
import sys

#Funcion que servira como llave para comparar en el sorted, hace que compare por numero.
def ordenNumerico(fn):
    if fn != 'renImages.py' and fn != 'renImages.py~':
        num  = os.path.splitext(fn)[0]
        image = num.split("_")
        res = int(image[1])
    return res


#Va renombrando los archivos en orden secuencial.
def rename(folder, orientation):
    if orientation == 'left':
        contador = 0
    else:
        contador = 1
    path = os.getcwd()+"/"+folder + "/" + orientation  
    ext = '.jpg'
    print("Renaming images...")
    for fn in sorted(os.listdir(path), key = ordenNumerico):
        os.rename(path+'/'+fn,folder+"/renamed/"+str(contador)+ext) 
        contador+=2
    print("Images renamed!")

