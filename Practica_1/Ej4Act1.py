#Ejercicio 4
#Dado un arreglo unidimensional de numeros enteros, ordenados crecientemente, escriba un programa que elimine todos los lementos repetidos.
#Considere que de haber valores, repetidos, estos se encontraran en posiciones consecutivas del arreglo.
numeros = [1,2,4,4,4,5,7,9,11,11,13,14,15,16,16]
sinrepetidos = []

for i in numeros:
    if i not in sinrepetidos:
        sinrepetidos.append(i)

print(sinrepetidos)
