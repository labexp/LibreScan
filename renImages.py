import os

#Funcion que servira como llave para comparar en el sorted, hace que compare por numero.
def ordenNumerico(fn):
    res = 3000
    if fn != 'renImages.py' and fn != 'renImages.py~':
        tmp  = os.path.splitext(fn)[0]
        numsName = tmp[4:]
        res = int(numsName)
    return res




#Va renombrando los archivos en orden secuencial.
def rename(folder,cnt):
    contador = cnt
    path = os.getcwd()+"/"+folder
    ext = '.jpg'
    for fn in sorted(os.listdir(path), key = ordenNumerico):
        if fn != 'renImages.py' and fn != str(contador)+ext:
            var = ''
            if contador < 10:
                var = '00'
            elif contador < 100:
                var = '0'
            else:
                var = ''
            os.rename(path+'/'+fn,var+str(contador)+ext) 
        contador+=2

rename("left",0)
rename("right",1)
