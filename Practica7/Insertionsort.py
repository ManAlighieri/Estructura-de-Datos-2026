def insertionsort(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1

        while j >= 0 and valor_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor_actual

ListaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
insertionsort(ListaN)
print("Lista ordenada: ", ListaN)