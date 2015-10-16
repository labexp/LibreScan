
import os
from shutil import copyfile

USERHOME = os.environ["HOME"]
RESOURCESPATH = 'resources/'
LIBRESCANPATH =  USERHOME + "/LibreScan"
LSCONFIGPATH =  USERHOME + "/.librescan"


def create_folders():
    os.mkdir(LIBRESCANPATH)
    os.mkdir(LSCONFIGPATH)


def create_config_files():
    config_template = RESOURCESPATH + "config_template.yaml"
    project_template = RESOURCESPATH + "project_template.yaml"
    copyfile(config_template, LSCONFIGPATH)
    copyfile(project_template, LSCONFIGPATH)
