import os

env_BASE_PYTHON = f"C:\\Users\\${os.getenv('USERNAME')}\\AppData\\Local\\Dinamica EGO 7\\PyEnvironment"
env_PYTHON_EXE =f"{env_BASE_PYTHON}\\python.exe"
env_FOLDER_DEV_PYTHON =f"{env_BASE_PYTHON}\\..\\pythonDinamica\\"
env_PYTHONHOME = env_BASE_PYTHON
env_PYTHON_INCLUDE = f"{env_BASE_PYTHON}\\include"
env_PYTHON_LIB = f"{env_BASE_PYTHON}\\Lib"
env_PYTHON_DLL = f"{env_BASE_PYTHON}\\DLLs"
env_PYTHONPATH =f"{env_BASE_PYTHON};{env_PYTHON_LIB};{env_PYTHON_INCLUDE};{env_PYTHON_DLL}"
env_PYTHONUSERBASE = env_BASE_PYTHON
env_PYTHONNOUSERBASE = env_BASE_PYTHON
env_PYTHONPLATLIBDIR = f"{env_BASE_PYTHON}\\Lib"
env_PIP_LIB = f"{env_PYTHONHOME}\\Lib\\site-packages\\pip\\__main__.py"
env_prefix=""
env_PYTHONWARNINGS = "ignore:DEPRECATION::pip._internal.cli.base_command"
env_PATH=f"{env_FOLDER_DEV_PYTHON};{env_PYTHONPATH};{env_PYTHONHOME};"+os.getenv('PATH', '')

availableVariables = locals()

def getDefaultEnvironmentVariables():
    env = {}
    default_variable_str = 'env_'
    for key in availableVariables.keys():
        if not key.startswith(default_variable_str):
            continue
        curVariableName = key[len(default_variable_str):]
        curVariableValue = os.getenv(curVariableName, availableVariables[key])
        env[curVariableName] = curVariableValue
        # os.environ[curVariableName] = curVariableValue
    return env

# def getEnvironments():
#     vars = {}
#     dict(globals())