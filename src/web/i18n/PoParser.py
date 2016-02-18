import polib
import os


class PoParser:

    @staticmethod
    def compile_po_files():
        file_path = os.path.realpath(__file__)
        locale_path = os.path.dirname(file_path)
        langs = os.listdir('{0}/locale'.format(locale_path))
        for lang in langs:
            path = '{0}/locale/{1}/LC_MESSAGES/messages'.format(locale_path, lang)
            po = polib.pofile(path + '.po')
            po.save_as_mofile(path + '.mo')
