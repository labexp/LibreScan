from os.path import exists as f_exists
from os import remove
from os import rename
from os import getenv


class OutputPreparer:

    def __init__(self):
        self.working_dir = None

    def _delete_pics(self):
        delete_pics_file = self.working_dir + "/.toDelete.ls"
        with open(delete_pics_file) as f:
            for filename in f:
                filename = filename[:-1]
                remove(self.working_dir + "/processed/" + filename + ".hocr")
                remove(self.working_dir + "/processed/" + filename + ".tif")
                remove(self.working_dir + "/raw/" + filename + ".jpg")
        f.close()

    def _rename_pics(self):
        rename_pics_file = self.working_dir + "/.pics.ls"
        pic_number = 1
        print(self.working_dir)
        with open(rename_pics_file) as f:
            for filename in f:
                filename = filename[:-1]
                pic_name = self.working_dir + "/processed/" + filename
                new_pic_name = "rlsp" + str(pic_number).zfill(5)
                new_pic_name = self.working_dir + "/processed/" + new_pic_name
                if (f_exists(pic_name + ".hocr") and
                        f_exists(pic_name + ".tif")):
                        rename(pic_name + ".hocr", new_pic_name + ".hocr")
                        rename(pic_name + ".tif", new_pic_name + ".tif")
                        pic_number += 1

    def run(self):
        self.working_dir = getenv("LS_PROJECT_PATH")
        self._delete_pics()
        self._rename_pics()
