@SET BASE_PYTHON=C:\Users\%USERNAME%\AppData\Local\Dinamica EGO 8\PyEnvironment
@SET FOLDER_DEV_PYTHON=%BASE_PYTHON%\..\pythonDinamica\
@SET PYTHONHOME=%BASE_PYTHON%
@SET PYTHON_INCLUDE=%PYTHONHOME%\include
@SET PYTHON_LIB=%BASE_PYTHON%\Lib
@SET PYTHON_DLL=%BASE_PYTHON%\DLLs
@SET PYTHONPATH=%BASE_PYTHON%;%PYTHON_LIB%;%PYTHON_INCLUDE%;%PYTHON_DLL%;%FOLDER_DEV_PYTHON%
@SET PYTHON_EXE=%PYTHONHOME%\python.exe
@SET PYTHONUSERBASE=%BASE_PYTHON%
@SET PYTHONNOUSERBASE=%BASE_PYTHON%
@SET PYTHONPLATLIBDIR=%BASE_PYTHON%\Lib
rem %PYTHONUSERBASE%;%BASE_PYTHON%\Lib;%BASE_PYTHON%\DLLs;%BASE_PYTHON%\Scripts;
@SET PIP_LIB=%PYTHONHOME%\Lib\site-packages\pip\__main__.py
@SET prefix=
@SET PYTHONWARNINGS=ignore:DEPRECATION::pip._internal.cli.base_command
@rem SET PYTHON_ARCH=64
@rem SET PYTHON_VERSION=3.8

@SET PATH=%FOLDER_DEV_PYTHON%;%PYTHONPATH%;%PYTHONHOME%;%PATH%
@rem disabled --user #was changing the output directory
@SET PIP_EXE="%PYTHON_EXE%" "%PIP_LIB%" install --disable-pip-version-check 
@rem Use: %%PIP_EXE%% LIBRARY_NAME ex: %%PIP_EXE%% requests
@rem %PIP_EXE% cpython cython segment_geospatial
@rem Daqui pra frente se digitar "python.exe" vai abrir o python do dinamica

curl --ssl-no-revoke -o "%FOLDER_DEV_PYTHON%\dinamicaClass.py" https://raw.githubusercontent.com/asfixia/DinamicaEGOUtils/master/dinamicaClass.py

@mkdir "%FOLDER_DEV_PYTHON%"

@explorer %FOLDER_DEV_PYTHON%
timeout 6 >NUL
start "DinamicaEGO With Python on terminal" /D "%FOLDER_DEV_PYTHON%" cmd