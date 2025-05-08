try:
    dinamica.inputs
except:
    from dinamicaClass import dinamicaClass
    dinamica = dinamicaClass({"s1": "ola", "t1": [["Key", "Value"], [1.0, 12.0], [2.0, 4.0]]})

print(dinamica.inputs)

dinamica.package('geopandas')

import geopandas as gpd

table = dinamica.inputs["t1"]

print(table)

string = dinamica.inputs["s1"]

print(string)

print('Sucesso')
