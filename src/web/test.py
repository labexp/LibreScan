import bottle, os
from bottle.ext.i18n import I18NPlugin, I18NMiddleware, i18n_defaults, i18n_view, i18n_template
from i18n.PoParser import PoParser
from jinja2 import Environment, FileSystemLoader
import bottle_i18n

i18n_defaults(bottle.SimpleTemplate, bottle.request)


def get():
    print(os.getcwd())
    jinja_env = Environment(loader=FileSystemLoader(searchpath='views/'), extensions=['pyjade.ext.jinja.PyJadeExtension'])
    app = bottle.Bottle()

    @app.route('/')
    def home():
        return jinja_env.get_template('prueba.jade').render(locals())

    '''
    @app.route('/')
    def index():
        return bottle.template("<b>{{_('hello')}} I18N<b/>?")'''

    @app.route('/world')
    def variable():
        return bottle.template("<b>{{_('hello %(variable)s', {'variable': world})}}<b/>?", {'world': app._('world')})


    @app.route('/view')
    @i18n_view('hello', function="i18n_view")
    def tmpl_app_hello():
        ''' '''
        return {}

    @app.route('/tmpl')
    def tmpl_app_hello():
        return i18n_template('hello', function="i18n_template")

    lang_app = bottle.Bottle()

    @lang_app.route('/')
    def sub():
        return bottle.template("current language is {{lang()}}")

    app.mount(app=lang_app, prefix='/lang', skip=None)

    return I18NMiddleware(app, I18NPlugin(domain='messages', default='pt', locale_dir='./i18n/locale'))


if __name__ == '__main__':
    supported_langs = ['pt', 'en', 'spa']
    PoParser.compilePoFiles(supported_langs)
    bottle.run(app=get(), host='localhost', port='8989', quiet=False, debug=True)
