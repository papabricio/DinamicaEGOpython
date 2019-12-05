import importlib
import pip

class dinamicaClass:

    inputs = {}

    outputs = {}

    def __init__(self, object):
        self.inputs = object
        pass

    def __str__(self):
        return 'dinamica'

    def install_whl(self, path):
        pip.main(['install', path])

    def install(package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])

    def package(self, *args):
        try:
            moduleName = args[0]
        except:
            moduleName = args[0]
        globals()[args[0]] = importlib.import_module(moduleName)


    def prepareTable(self, *args):
        pass
