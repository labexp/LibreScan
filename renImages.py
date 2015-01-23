import os
import sys

#Funcion que servira como llave para comparar en el sorted, hace que compare por numero.
def ordenNumerico(fn):
    if fn != 'renImages.py' and fn != 'renImages.py~':
        num  = os.path.splitext(fn)[0]
        res = int(num)
    return res


#Va renombrando los archivos en orden secuencial.
def rename(folder, orientation):
    if orientation == 'left':
        contador = 0
    else:
        contador = 1
    path = os.getcwd()+"/"+folder + "/" + orientation  
    ext = '.jpg'
    for fn in sorted(os.listdir(path), key = ordenNumerico):
        if fn != 'renImages.py' and fn != str(contador)+ext:
            os.rename(path+'/'+fn,str(contador)+ext) 
        contador+=2


rename("test2","left")

