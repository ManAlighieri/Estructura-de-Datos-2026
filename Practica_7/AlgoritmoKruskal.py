aristas = [
    (1,  6, 2),
    (2,  5, 6),
    (3,  4, 1),
    (4,  3, 6),
    (5,  0, 4),
    (6,  7, 1),
    (7,  2, 5),
    (8,  2, 6),
    (9,  1, 5),
    (10, 1, 6),
    (11, 1, 5),
    (12, 3, 5),
    (13, 7, 1),
    (14, 4, 1),
    (15, 0, 4),
    (16, 7, 3),
    (17, 3, 6),
    (18, 0, 7),
]

def encontrar(padre, i):
    if padre[i] != i:
        padre[i] = encontrar(padre, padre[i])
    return padre[i]

def unir(padre, rango, x, y):
    rx, ry = encontrar(padre, x), encontrar(padre, y)
    if rango[rx] < rango[ry]:
        padre[rx] = ry
    elif rango[rx] > rango[ry]:
        padre[ry] = rx
    else:
        padre[ry] = rx
        rango[rx] += 1

def kruskal(num_nodos, aristas):
    aristas_ordenadas = sorted(aristas, key=lambda x: x[0])
    padre = list(range(num_nodos))
    rango = [0] * num_nodos
    mst = []
    costo_total = 0

    for peso, u, v in aristas_ordenadas:
        ru, rv = encontrar(padre, u), encontrar(padre, v)
        if ru != rv:
            unir(padre, rango, ru, rv)
            mst.append((u, v, peso))
            costo_total += peso
        if len(mst) == num_nodos - 1:
            break

    print(f"Aristas del MST: {mst}")
    print(f"Costo total: {costo_total}")
    return mst, costo_total

mst, costo = kruskal(num_nodos=8, aristas=aristas)