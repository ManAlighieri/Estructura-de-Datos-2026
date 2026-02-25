#Representar una sala con una matriz Asientos [F,C] booleana, donde FALSO = libre y VERDADERO = reservar

#Entradas
# Dimensiones F y C
# K operaciones en formato: RESERVA(I,J), LIBERAR(I,J), CONSULTAR(I,J)

#Salida
#Mensaje por operacion (exito o razon de rechazo)
#Total de asientos reservados al final
#Fila con mas asientos reservados 

F = 6
C = 6   

ASIENTOS = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

def reservar(i, j):
    if ASIENTOS[i-1][j-1] == 0:
        ASIENTOS[i-1][j-1] = 1
        return (f"Aceptado : ({i}, {j}) Reservado")
    else:
        return (f"Rechazado : ({i}, {j}) Ya reservado")

def liberar(i, j):
    if ASIENTOS[i-1][j-1] == 1:
        ASIENTOS[i-1][j-1] = 0
        return (f"Aceptado : ({i}, {j}) Liberado")
    else:
        return (f"Rechazado : ({i}, {j}) Asiento ya libre")

def consultar(i, j):
    if ASIENTOS[i-1][j-1] == 0:
        return (f"({i}, {j}) Asiento libre")
    else:
        return (f"({i}, {j}) Asiento reservado")

print(reservar(1,1))
print(reservar(1,2))
print(reservar(1,1))
print(consultar(1,1))
print(liberar(1,1))
print(liberar(1,1))
print(reservar(3,4))
print(reservar(6,6))
print(consultar(6,6))
print(reservar(2,5))

total = 0
for fila in ASIENTOS:
    for asiento in fila:
        if asiento == 1:
            total += 1
print(f"Total de asientos reservados: {total}")

max_reservados = 0
fila_mayor = 0

for i in range(F):
    contador = 0
    for j in range(C):
        if ASIENTOS[i][j] == 1:
            contador += 1

    if contador > max_reservados:
        max_reservados = contador
        fila_mayor = i + 1
print(f"Fila con más asientos reservados: {fila_mayor}")