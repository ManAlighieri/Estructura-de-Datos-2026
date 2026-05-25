import heapq

grafo = {
    0: [(2, 20), (1, 10)],
    1: [(0, 10), (2, 20), (4, 20), (3, 50)],
    2: [(0, 20), (4, 33), (1, 20), (3, 10)],
    3: [(2, 10), (4, 20), (1, 50), (5, 2)],
    4: [(2, 33), (1, 20), (3, 20), (5, 1)],
    5: [(4, 1), (3, 2)],
}

def prim(grafo, inicio):
    visitados = set()
    mst = []
    costo_total = 0

    print(f"root({inicio})")

    heap = [(0, 0, inicio, inicio)]

    while heap:
        neg_orig, peso, origen, nodo = heapq.heappop(heap)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if origen != nodo:
            print(nodo)
            mst.append((origen, nodo, peso))
            costo_total += peso

        for vecino, w in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(heap, (-nodo, w, nodo, vecino))

    return mst, costo_total

mst, costo_total = prim(grafo, inicio=2)