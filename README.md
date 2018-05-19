# LibreScan

## Comunidad
- Hemos creado un bot de telegram para mantener a todos informados sobre los avances del proyecto, agrega el bot `@Librescan_bot` para recibir notificaciones. Creditos a nuestro amigo [Lupa18](https://github.com/lupa18) por nuestro bot de telegram! 

## Instalación con Docker (Recomenda)

Por favor refierase a la documentación de docker para su instalación:
 
- https://docs.docker.com/install
- [How can I use docker without sudo?](https://askubuntu.com/a/477554)

Una vez instalado `docker` basta con correr el comando:

```bash
docker run -d -p 8080:8080 --privileged --name librescan \
-v ~/LibreScanProjects:/root/LibreScanProjects \
-v ~/.librescan:/root/.librescan \
-v /dev/bus/usb:/dev/bus/usb \
labexperimental/librescan:v1.2.0
```

Después de correr el comando encontará dos nuevas carpetas en su directorio `HOME`:

- `~/LibreScanProjects`: Dirección donde se almacenan los proyectos e imágenes.
- `~/.librescan`: Dirección donde se almacena la configuración general de LS.

Una vez creado el contenedor de librescan no es necesario volver a correr el comando anterior,
puede utilizar los siguientes comandos para administrar el contenedor:

- Ejecute el siguiente comando para detener el contenedor:
    
      docker container stop librescan  

- Ejecute el siguiente comando para volver a iniciar el contenedor cuando lo desee:
    
      docker container start librescan 

## Instalación Manual

### ! Nota importante antes de iniciar

Este tipo de instalación está sujeta a cambios dependiendo la distribución de linux que el usuario
tenga en su computador, recomendamos intentar instalar la version de docker donde hemos
preparado todo para su correcto funcionamiento.

Si desea continuar con la instalación manual, algunas de las versiones mencionadas pueden variar
con el tiempo o la distribución de linux. Si encuentra algún problema durante la instalación puede
abrir un issue o bien diriguirse a nuestro canal de Telegram para recibir ayuda.


### Instrucciones

- Instalar dependencias que serán utilizadas:

		# apt-get install python3-pip lua5.2 liblua5.2 git-svn libusb-dev python3 python-dev libjpeg8 libffi-dev libturbojpeg1-dev

--------------------------------------------------------------------------------------------

- Instalar tesseract-ocr para el reconocimiento de texto:

		# apt-get install tesseract-ocr

	Nota: Para más idiomas se instala de esta forma (Ejemplo con español): 

		# apt-get install tesseract-ocr-spa (Para Español) 

--------------------------------------------------------------------------------------------

- Instalar scantailor para el procesamiento de las fotos:

		# apt-get install scantailor
	
	Nota: Si no se encuentra en los repositorios agregar este a /etc/apt/sources.list: 

		- deb http://http.debian.net/debian wheezy-backports main

		Posteriormente hacer un # apt-get update

--------------------------------------------------------------------------------------------

- Instalar pdfbeads para generar pdfs a partir de tifs+hocr:

		# apt-get install ruby ruby-dev ruby-rmagick 
		# gem install iconv pdfbeads

	Nota: Si presenta errores al instalar pdfbeads relacionados con zlib, instalar:

		# apt-get install zlib1g-dev

--------------------------------------------------------------------------------------------
- En cuanto a las cámaras hay que instalar el CHDKPTP en el sistema.

		$ git clone https://github.com/svn2github/chdkptp.git

		$ cd chdkptp

		$ mv config-sample-linux.mk config.mk

		$ make

		# mkdir /usr/bin/chdkptp

		# cp chdkptp.sh /usr/bin/chdkptp/chdkptp

      -- nota: chdkptp.sh está en la dirección donde se descargó el chdkptp.

		# nano /usr/bin/chdkptp/chdkptp

    Modificar la línea que dice
    
      CHDKPTP_EXE=chdkptp
      CHDKPTP_DIR=/path/to/chdkptp
    
    por:
    
      CHDKPTP_EXE=chdkptp.sh
      CHDKPTP_DIR=<ubicación del folder clonado de chdkptp> (Y guardamos los cambios)
    
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

--------------------------------------------------------------------------------------------
- Una vez instaladas todas las dependencias, procedemos a clonar el repositorio de LibreScan.

		$ git clone https://github.com/LabExperimental-SIUA/LibreScan.git

- Nos metemos a la carpeta clonada, y al código fuente.

		$ cd LibreScan/src

- Instalamos las dependencias de Python
        
      $ pip3 install -r requirements.txt

- Corremos el setup para la creación de carpetas y archivos de configuración.

      $ python3 setup.py
		
- Para ejecutar la aplicación web

		$ python3 main.py web

- Por último, abrimos el navegador en http://0.0.0.0:8080
