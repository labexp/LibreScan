# LibreScan

### Instalation

- Install the dependencies that will be used.

		# apt-get install python3-pip lua5.2 liblua5.2 git-svn libusb-dev python3 python-dev libjpeg8 libffi-dev libturbojpeg1-dev

		# pip3 install pyYAML bottle pyjade jinja2 polib cffi pexpect

		# pip3 install jpegtran-cffi==0.5.2

--------------------------------------------------------------------------------------------

- Install tesseract-ocr for text recognition:

		# apt-get install tesseract-ocr

	Note: To install other languages its done this way (For example in Spanish): 

		# apt-get install tesseract-ocr-spa 

--------------------------------------------------------------------------------------------

- Install scantailor for photo processing:

		# apt-get install scantailor
	
	Note: If the repositories can't be found use this one /etc/apt/sources.list: 

		- deb http://http.debian.net/debian wheezy-backports main

		Remember to use # apt-get update

--------------------------------------------------------------------------------------------

- Install pdfbeads to generate pdfs from tifs+hocr:

		# apt-get install ruby ruby-dev ruby-rmagick 
		# gem install iconv pdfbeads


--------------------------------------------------------------------------------------------
- For the camreras CHDKPTP must be installed.

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

Modify this line:

    #CHDKPTP_DIR=/path/to/chdkptp

for: 
	
	CHDKPTP_DIR=<ClonedFolder>/chdkptp (And save the changes)

note: <ClonedFolder>/chdkptp is the directory where CHDKPTP was cloned (the first step of this section). 

		# ln -s /usr/bin/chdkptp/chdkptp /bin

--------------------------------------------------------------------------------------------

Its necessary to have CHDK installed in the cameras. (In case of not having it you can follow this guide. We recommend to use the method "a"):
https://github.com/LabExperimental-SIUA/ilt/wiki/Instalaci%C3%B3n-de-CHDK 

To know which camera is the right one or the left one we create a file called
'orientation.txt', in which is stored in the camera's SD card root directory.
For now this process must be done manually by inserting the SD card to
the computer and create the file. 
Steps:

1. Make sure the SD card is unblocked.
2. Create a file called orientation.txt in the root of the SD card and
inside the file write the word 'left' without quotes. This SD card will
be used for the left camera.
3. Create a file called orientation.txt in the root of the SD card and
inside the file write the word 'right' without quotes. This SD card will
be used for the right camera.

Note: We're currently working to make this process automatic.
By just connecting the cameras you can decide the orientation
without creating the files manually.

--------------------------------------------------------------------------------------------
### Configuration and usage


- Once we install all the dependencies, we can clone LibreScan.(For now the develop branch).

		$ git clone https://github.com/LabExperimental-SIUA/LibreScan/tree/develop

- We enter to the cloned folder and head to

		$ cd LibreScan/src

- Run the setup to create the folders and files for the configuration.

		$ python3.4 setup.py
		
**NOTE: All the previous steps should only be done once!**
		
- To run the web application

		$ python3.4 main.py web

- Open in your web browser http://0.0.0.0:8180

