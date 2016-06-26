# LibreScan

LibreScan is a Free Software project developed at Centro Académico de Alajuela's Laboratorio Experimental (one of the Instituto Tecnológico de Costa Rica's sites). This research project involves the development of a software that groups different tools with specific functions to complete the document scanning workflow. The main goal of LibreScan is to promote the free access to knowledge and education, by providing a non-cost free software that allows people to follow the digitization process that includes capturing photos, image processing and digital document generation.

## Installation

The software is currently working in Debian 8 Jessie. There are two ways to install LibreScan:

1. Brief way:

	- Clone this repository:
	
			$ git clone https://github.com/LabExperimental-SIUA/LibreScan.git
	
	- Enter the cloned folder:
	
			$ cd LibreScan
	
	- As root, overwrite the OS sources.list file:
	
			# cp apt.sources /etc/apt/sources.list

	- Update repositories:

			# apt-get update
	
	- Grant execution permission to the sh file:
	
			# chmod +x Dependencies.sh
	
	- Execute the script:
	
			# sh Dependencies.sh
--------------------------------------------------------------------------------------------

2. Manual way:

	- Install the dependencies that will be used.
			
			# apt-get install python3-pip lua5.2 liblua5.2 git-svn libusb-dev python3 python-dev libffi-dev libturbojpeg1-dev libssl-dev libjpeg8-dev libjpeg8
	
			# pip3 install pyYAML bottle pyjade jinja2 polib cffi pexpect
	
			# pip3 install jpegtran-cffi==0.5.2
	
	--------------------------------------------------------------------------------------------
	
	- Install tesseract-ocr for text recognition:
	
			# apt-get install tesseract-ocr
	
		Note: To install other languages (e.g. spanish): 
	
			# apt-get install tesseract-ocr-spa 
	
	--------------------------------------------------------------------------------------------
	
	- Install scantailor for photo processing:
	
			# apt-get install scantailor
	
	--------------------------------------------------------------------------------------------
	
	- Install pdfbeads to generate pdfs from tifs+hocr:
	
			# apt-get install ruby ruby-dev ruby-rmagick 
			# gem install iconv pdfbeads
	
	
	--------------------------------------------------------------------------------------------
	- CHDKPTP must be installed for the cameras.
	
			$ git svn clone http://subversion.assembla.com/svn/chdkptp/trunk chdkptp
	
			$ cd chdkptp
	
	    -- note: al 01.02.2015 Checked out HEAD:
	       http://subversion.assembla.com/svn/chdkptp/trunk r694
	
			$ mv config-sample-linux.mk config.mk
	
			$ make
	
			# mkdir /usr/bin/chdkptp
	
			# cp chdkptp-sample.sh /usr/bin/chdkptp/chdkptp
	
	      -- note: chdkptp-sample.sh is at the path where chdkptp was downloaded.
	
			# nano /usr/bin/chdkptp/chdkptp
	
	Modify the line:
	
	    #CHDKPTP_DIR=/path/to/chdkptp
	
	for: 
		
		CHDKPTP_DIR=<ClonedFolder>/chdkptp (And save the changes)
	
	note: /chdkptp is the directory where CHDKPTP was cloned (the first step of this section). 
	
			# ln -s /usr/bin/chdkptp/chdkptp /bin
	
	--------------------------------------------------------------------------------------------
	
	It's necessary to have CHDK installed in the cameras. (In case of not having it you can follow this guide. We recommend to use the method "a"):
	https://github.com/LabExperimental-SIUA/ilt/wiki/Instalaci%C3%B3n-de-CHDK 
	
	To know which camera is the right one or the left one we create a file called
	'orientation.txt', which is stored in the root directory of the camera's SD card.
	For now this process must be done manually by inserting the SD card in 
	the computer and creating the file. Steps:
	
	1. Make sure the SD card is unblocked.
	2. Create a file called orientation.txt in the root of the SD card and
	inside the file write the word 'left' without quotes. This SD card will
	be used for the left camera.
	3. (Other camera) Create a file called orientation.txt in the root of the SD card and
	inside the file write the word 'right' without quotes. This SD card will
	be used for the right camera.
	
	Note: We're currently working to make this process automatic.
	By just connecting the cameras you can decide the orientation
	without creating the files manually.

	- Clone this repository:

			# git clone https://github.com/LabExperimental-SIUA/LibreScan.git

--------------------------------------------------------------------------------------------
## Configuration and usage

- We enter to the cloned folder and head to

		$ cd LibreScan/src

- Run the setup to create the folders and files for the configuration.

		$ python3.4 setup.py
		
**NOTE: All the previous steps should only be done once!**
		
- To run the web application

		$ python3.4 main.py web

- Open in your web browser http://0.0.0.0:8180

