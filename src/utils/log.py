import logging
import os.path


class Log:
    def __init__(self):
        homedir = os.path.expanduser('~')
        logging.basicConfig(filename=homedir + '/.librescan/librescan.log',format = '%(asctime) - s %(levelname)s:%(message)s',level=logging.DEBUG)


    def log_error(self, p_message):
        logging.error(p_message)

#logger types
#logging.debug('debug message')
#logging.info('info message')
#logging.warn('warn message')
#logging.error('error message')
#logging.critical('critical message')	

