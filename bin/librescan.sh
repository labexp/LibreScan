#!/bin/bash

# Kill all other running instances
kill `ps aux | grep main.py | grep -v 'grep' |  awk '{print $2}' | xargs`

# Se pasa al directorio de LibreScan
cd /usr/share/LibreScan/src/

#check if running the setup is necesary
if [ ! -d $HOME/.librescan/ ]
then 
	python3 setup.py
fi;

# Run the application
python3 main.py web
