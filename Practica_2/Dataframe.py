import pandas as pd

#Leer archivo CSV delimitado por comas (por defecto)
df = pd.read_csv('Housing.csv')

#Mostrar las primeras 5 filas
print(df.head())

