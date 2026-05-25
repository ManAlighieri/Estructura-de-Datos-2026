from collections import deque

datos_tareas = [
    ('T1', 1, 0),
    ('T2', 0, 0),
    ('T3', 2, 0),
    ('T4', 1, 0),
    ('T5', 2, 2),
    ('T6', 2, 1),
]

bicola = deque()

for tarea in datos_tareas:
    bicola.appendleft(list(tarea))

print(bicola)

while bicola:
    tarea_actual = bicola.popleft()
    nombre_tarea = tarea_actual[0]
    fallos = tarea_actual[1]

    if fallos == 0:
        print("Procesando la tarea", nombre_tarea, "= Procesada Correctamente")
    else:
        tarea_actual[1] -= 1
        tarea_actual[2] += 1
        bicola.appendleft(tarea_actual)
        print("Procesando la tarea", nombre_tarea, "= Fallo")

print("--------------------------------------------------")

