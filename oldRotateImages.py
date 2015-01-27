import logging
import shutil
import pyexiv2
import os
from wand.image import Image

#Funcion reutilizada de autorotate.py de spreads para rotar las imagenes una vez tomadas con chdkptp.
def autorotate_image(in_path, out_path):
	try:
		metadata = pyexiv2.ImageMetadata(in_path)
		metadata.read()
		
		orient = int(metadata['Exif.Image.Orientation'].value)
		print metadata
		print orient
	except:
		return

	img = Image(filename=in_path)
	if orient == 1:
		shutil.copyfile(in_path, out_path)
		return
	elif orient == 2:
		img.flip()
	elif orient == 3:
		img.rotate(180)
	elif orient == 4:
		img.flop()
	elif orient == 5:
		img.rotate(90)
		img.flip()
	elif orient == 6:
		img.rotate(90)
	elif orient == 7:
		img.rotate(270)
		img.flip()
	elif orient == 8:
		img.rotate(270)
	img.save(filename=out_path)


#Rota todas las imagenes del directorio actual y las coloca en una carpeta creada llamada rotated.
def rotateImages(folder):
    path = os.getcwd()+"/"+folder+"/"+"renamed"
    print("Rotating images...")
    arr = os.listdir(path)
    percentage = 100/len(arr)
    progress = 0
    for fn in arr:
        autorotate_image(path+"/"+fn,os.getcwd()+"/"+folder+"/"+"rotated/"+os.path.splitext(fn)[0]+"_rotated.jpg")
        progress+=percentage
        print(str(progress)+"%")
    print("100% \nRotation successful!")


rotateImages("book_201501232231")