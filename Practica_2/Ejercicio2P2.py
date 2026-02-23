import pandas as pd
import numpy as np

#Leer archivo CSV delimitado por comas (por defecto)
df = pd.read_csv('./Housing.csv')

#Mostrar las primeras 5 filas
#lista = df['price'].tolist()

#Ejemplo usando las formulas
#def housingStats(str):
    #print(df[str].mode()) #moda
    #print(df[str].var()) #varianza
    #desviacion_estandar = np.sqrt(df[str].var()) 
    #print(desviacion_estandar)

def housingStats(str):
    lista = df[str].tolist()
    media(lista)
    moda(lista)
    varianza(lista)
    desviacion_estandar(lista)

def media(lista):
    suma = 0
    for i in lista:
        suma += i
    media = suma / len(lista)
    return print("Media: ", media)

def moda(lista):
    frecuencia = {}
    for i in lista:
        frecuencia[i] = frecuencia.get(i, 0) + 1
        moda = max(frecuencia, key=frecuencia.get)
    return  print("Moda: ", moda)

def varianza(lista):
    media = sum(lista) / len(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return  print("Varianza: ", varianza)

def desviacion_estandar(lista):
    media = sum(lista) / len(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    desviacion_estandar = varianza ** 0.5
    return  print("Desviacion estandar: ", desviacion_estandar)

housingStats('price')