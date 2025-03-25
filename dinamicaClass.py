import importlib
import time
import pip
import os
import subprocess
import re
import json
import inspect

try:
    from dinamicaEnvironments import getDefaultEnvironmentVariables
    defaultEnv = getDefaultEnvironmentVariables()
    for key in defaultEnv.keys():
        if key not in os.environ:
            os.environ[key] = defaultEnv[key]
except Exception as e:
    print(e)
    pass

class Mutex:
    def __init__(self, mutex_file):
        self.mutex_file = mutex_file
        self.mutex_map = None

    def acquire(self):
        while True:
            try:
                self.mutex_map = open(self.mutex_file, "w")
                return
            except OSError:
                pass
            time.sleep(0.1)

    def release(self):
        if self.mutex_map is not None:
            self.mutex_map.close()
            self.mutex_map = None

lock_file = 'python_lock_multiprocess'

class dinamicaClass:

    inputs = {}

    outputs = {}

    def __init__(self, object):
        self.inputs = object
        pass

    def __str__(self):
        return 'dinamica'

    def install_pip(self, package_name):
        command = ['"'+os.getenv('PYTHON_EXE')+'"', '"'+os.getenv('PIP_LIB')+'"', "install", "--disable-pip-version-check", package_name]
        try:
            mutex = Mutex(lock_file)
            mutex.acquire()
            subprocess.check_call(" ".join(command), env=os.environ)
            print(f"Successfully installed {package_name}")
            mutex.release()
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package_name}: {e}")
        finally:
            print("Install command: " + ' '.join(command))

    def install_whl(self, path):
        pip.main(['install', path])

    def install(self, package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            if hasattr(pip._internal.main, 'main'):
                pip._internal.main.main(['install', package])
            else:
                pip._internal.main(['install', package])

    def package(self, *args):
        def getLibName(possibleName):
            return re.split('[><=~]', possibleName)[0]
        pipParams = args[1] if len(args)>=2 and args[1] is not None and len(args[1])>0 else args[0]
        importName = args[2] if len(args)>=3 and args[2] is not None and len(args[2])>0 else getLibName(args[0])
        libraryPackageName = getLibName(importName)
        try:
            globals()[importName] = importlib.import_module(libraryPackageName)
            print("Library loaded " + importName)
        except:
            self.install_pip(pipParams)
            globals()[importName] = importlib.import_module(libraryPackageName)

        # Inject into caller's globals
        caller_frame = inspect.currentframe().f_back
        caller_globals = caller_frame.f_globals
        caller_globals[importName] = globals()[importName]


    def prepareTable(self, *args):
        pass

    def writeOutput(self, filePath):
        json.dump(self.outputs, open(filePath, "w"))
