# DinamicaEGOutils

 Procedure to run DinamciaEGO python outside Dinamica

 - setEnv.bat: set environment variables to use DinamicaEGO python
## How to use it:
clone or download this repository:

```
git clone https://github.com/papabricio/DinamicaEGOpython.git
```

```
cd DinamicaEGOpython
```
```
./setEnv.bat
```

At the end of the script exceution a cmd terminal will open. Run your codes or open your code editor from this terminal, all  environment variables will be inherited

Configure your code editor or IDE to use DinamicaEGO python interpreter. Check it with:
```
where python
```

# Python Integration
- dinamicaClass.py : Class that allows get the python scripts used in dinamica to be editable in an external python IDE.
> You have to first configure your IDE to use the same Environment as DinamicaEGO, then:
> 
> In your python script in DinamicaEGO add at the beginning the following line:
> ```
> from pprint import pprint
> pprint(dinamica.inputs)
> ```
> In your IDE copy the dinamicaClass.py to your directory, and
>   1. add the following content before your script:
> ```
> from dinamicaClass import dinamicaClass
> dinamica = dinamicaClass({...})
> ```
>   2. Run the model in Dinamica, and copy the pprint() result from the dinamica log and replace the {...} in your IDE script.

