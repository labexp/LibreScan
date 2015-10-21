import polib


class PoParser:

    @staticmethod
    def compilePoFiles():
        langs = ['pt', 'en', 'spa']
        for lang in langs:
            path = './i18n/locale/' + lang + '/LC_MESSAGES/messages'
            po = polib.pofile(path + '.po')
            po.save_as_mofile(path + '.mo')