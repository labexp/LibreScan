# LibreScan

LibreScan es un proyecto de Software Libre desarrollado en el Laboratorio Experimental del Centro Académico de Alajuela, sede del Instituto Tecnológico de Costa Rica. Este proyecto de investigación consiste en la elaboración de un software que agrupa distintas herramientas que cumplen funciones específicas dentro del flujo de tareas necesarias para escanear un documento. El objetivo de LibreScan es promover el acceso libre al conocimento y la educación, al proveer un software libre y gratuito que permita realizar el proceso de captura de fotos, procesamiento y generación de un documento digital.

## Instalación

Actualmente el software funciona en el sistema operativo Debian 8 Jessie. Existen dos formas de instalar LibreScan:

1. Forma resumida:

- Clonar este repositorio:

		$ git clone https://github.com/LabExperimental-SIUA/LibreScan.git

- Entrar en la carpeta clonada:

		$ cd LibreScan

- Como root, sobreescribir el sources.list del sistema operativo

		# cp apt.sources /etc/apt/sources.list

- Dar permisos de ejecución al script Dependencies.sh:

		# chmod +x Dependencies.sh

- Ejecutar el script de instalación de dependencias:

		# sh Dependencies.sh

2. Forma manual:

- Instalar dependencias que serán utilizadas:
		
		# apt-get install python3-pip lua5.2 liblua5.2 git-svn libusb-dev python3 python-dev libffi-dev libturbojpeg1-dev libssl-dev libjpeg8-dev libjpeg8		

		# pip3 install pyYAML bottle pyjade jinja2 polib cffi pexpect

		# pip3 install jpegtran-cffi==0.5.2

--------------------------------------------------------------------------------------------

- Instalar tesseract-ocr para el reconocimiento de texto:

		# apt-get install tesseract-ocr

	Nota: Para más idiomas se instala de esta forma (Ejemplo con español): 

		# apt-get install tesseract-ocr-spa (Para Español) 

--------------------------------------------------------------------------------------------

- Instalar scantailor para el procesamiento de las fotos:

		# apt-get install scantailor

		Posteriormente hacer un # apt-get update

--------------------------------------------------------------------------------------------

- Instalar pdfbeads para generar pdfs a partir de tifs+hocr:

		# apt-get install ruby ruby-dev ruby-rmagick 
		# gem install iconv pdfbeads


--------------------------------------------------------------------------------------------
- En cuanto a las cámaras hay que instalar el CHDKPTP en el sistema.

		$ git svn clone http://subversion.assembla.com/svn/chdkptp/trunk chdkptp

		$ cd chdkptp

    -- nota: al 01.02.2015 Checked out HEAD:
       http://subversion.assembla.com/svn/chdkptp/trunk r694

		$ mv config-sample-linux.mk config.mk

		$ make

		# mkdir /usr/bin/chdkptp

		# cp chdkptp-sample.sh /usr/bin/chdkptp/chdkptp

      -- nota: chdkptp-sample.sh está en la dirección donde se descargó el chdkptp.

		# nano /usr/bin/chdkptp/chdkptp

Modificar la línea que dice

    #CHDKPTP_DIR=/path/to/chdkptp

por: 
	
	CHDKPTP_DIR=<FolderClonado>/chdkptp (Y guardamos los cambios)

nota: <FolderClonado>/chdkptp es la dirección donde se haya clonado el chdkptp (en el primer paso de esta sección). 

		# ln -s /usr/bin/chdkptp/chdkptp /bin

--------------------------------------------------------------------------------------------
- Es necesario tener CHDK instalado en las cámaras. (En caso de no tenerlo se puede seguir esta guía. Se recomienda usar el método "a"): 
https://github.com/LabExperimental-SIUA/ilt/wiki/Instalaci%C3%B3n-de-CHDK 




- Para reconocer cuál cámara es la derecha y cuál es la izquierda hacemos uso de un archivo 'orientation.txt', que se encuentra almacenado la raíz de la tarjeta SD de cada cámara. Por ahora este proceso se debe hacer manualmente, introduciendo la SD en la computadora y creando el archivo manualmente. Pasos:
	
	1. Asegurarse que la SD esté desbloqueada.
	2. Para la cámara que desea usar al lado izquierdo, crear un archivo orientation.txt que tenga la palabra 'left' (sin comillas) como contenido.
	3. Para la cámara que desea usar al lado derecho, crear un archivo orientation.txt que tenga la palabra 'right' (sin comillas) como contenido.

Nota: Estamos trabajando en automatizar este proceso, de modo que se el usuario conecte las cámaras y decida la orientación sin crear el archivo manualmente.

- Clonar el repositorio:

		$ git clone https://github.com/LabExperimental-SIUA/LibreScan.git

--------------------------------------------------------------------------------------------
## Configuración y Uso

- Nos metemos al código fuente de la carpeta clonada:

		$ cd LibreScan/src

- Corremos el setup para la creación de carpetas y archivos de configuración.

		$ python3.4 setup.py
		

**NOTA: los pasos anteriores solo deben ser ejecutados una vez.**
		
- Para ejecutar la aplicación web

		$ python3.4 main.py web

- Por último, abrimos el navegador en http://0.0.0.0:8180

