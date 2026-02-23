A = [
    [4, 7, 2, 9, 5, 7],
    [1, 3, 7, 6, 8, 0],
    [9, 2, 5, 7, 4, 6],
    [8, 7, 1, 3, 7, 2],
    [5, 0, 6, 4, 2, 9],
    [7, 8, 9, 2, 1, 7]
]

#valor = 7

#listadecoordenadas = []

#for i in range(len(A[0])):
    #for j in range(len(A[0])):
        #if A[i][j] == valor:
            #listadecoordenadas.append((i+1, j+1))
#if listadecoordenadas == []:
    #print("No encontrado")
#else:    
    #print(listadecoordenadas)


def coordenadas(A, valor):
    listadecoordenadas = []
    for i in range(len(A[0])):
        for j in range(len(A[0])):
            if A[i][j] == valor:
                listadecoordenadas.append((i+1, j+1))
    if listadecoordenadas == []:
        return "No encontrado"
    else:    
        return print(listadecoordenadas)

coordenadas(A, 7)
