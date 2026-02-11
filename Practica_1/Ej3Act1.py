#___Ejercicio 3___
#Dada una cadena de caracteres como dato, se dea saber el umero de veces que aparecen las letras 'a', 'b' y 'A', 'B',...,'Z' en dicha cadena.
#Escriba un programa que resuelva el problema
#Sin Arreglo
cadena = "Parangaricutirimicuaro"
cadena.lower()
letras = "abcdefghijklmnopqrstuvwxyz"

for i in letras:
    cantidad = cadena.count(i)
    if cantidad > 0:
        print(i, ":", cantidad)

#Arreglos
cadena = "Parangaricutirimicuaro"
letras = []
cantidades = []

for x in cadena:
    if x not in letras:
        letras.append(x)
        cantidades.append(1)
    else:
        indice = letras.index(x)
        cantidades[indice] += 1

for i in range(len(letras)):
    print(letras[i], ":", cantidades[i])