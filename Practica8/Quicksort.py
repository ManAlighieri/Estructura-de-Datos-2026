def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]

    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]

    return quicksort(izquierda) + centro + quicksort(derecha)

ListaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
print(quicksort(ListaN))