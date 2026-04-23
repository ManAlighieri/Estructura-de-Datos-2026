from collections import deque 
 
def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 

    print(f"{'Lista (vecinos)':<25} {'Cola'}")
    print("-" * 50)
 
    while queue:
        node = queue.popleft() 
        if node not in visited: 
            visited.add(node) 
            for neighbor in graph[node]: 
                if neighbor not in visited: 
                    queue.append(neighbor)
            print(f"{node}:{str(graph[node]):<22} {list(queue)}")
grafo = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": [], "E": [], "F": [], "G": []
}
    
bfs(grafo, "A")