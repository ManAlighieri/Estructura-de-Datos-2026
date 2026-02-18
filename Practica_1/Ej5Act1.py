#Ejercicio 5
A = [[5,6,13],
     [1,10,1],
     [1,11,3]]

B = [[1,2,1],
     [6,5,13],
     [3,11,12]]

resul = []
for i in range(len(A)):
    fi1 = []
    for j in range(len(A[0])):
        C = 0
        for x in range(len(B)):
            C+= A[i][x] * B[x][j]
            fi1.append(C)
        resul.append(C)
print(resul)

