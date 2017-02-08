#!/usr/bin/python

from web.i18n.PoParser import PoParser
from web.libreScanWeb import LibreScanWeb
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You most provide at least one argument.')
        print('Usted debe de proveer al menos un argumento.')
        sys.exit(0)

    if sys.argv[1] == 'web':
        app = LibreScanWeb()
        app.run_app()
    else:
        print('Argument not valid.')
        print('El argumento ingresado no es válido.')
