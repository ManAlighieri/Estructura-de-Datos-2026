A = [
    [4,7,2,9,5,7],
    [1,3,7,6,8,0],
    [9,2,5,7,4,6],
    [8,7,1,3,7,2],
    [5,0,6,4,2,9],
    [7,8,9,2,1,7]
]

X = 7

coordenadas = []

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == X:
            coordenadas.append((i+1, j+1))

if coordenadas == []:
    print("El valor no se encuentra en la matriz.")
else:
    print(coordenadas)