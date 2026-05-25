from collections import deque

def bfs(graph, start):
    visitado = set([start])
    queue = deque([start])
    lista = []

    print(*queue)

    while queue:
        node = queue.popleft()
        lista.append(node)

        for nx in graph[node]:
            if nx not in visitado:
                visitado.add(nx)
                queue.append(nx)

        print(*queue)

    print(*lista)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

bfs(graph, 'A')