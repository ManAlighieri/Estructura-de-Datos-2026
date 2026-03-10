from collections import deque

cola = deque(maxlen=3)
limite = 10
tiempo = [0, 2, 4, 6, 12]

for x in tiempo:
    print("\nLlega", x)

    if cola and x - cola[0] >= limite:
        while cola:
            print("dequeue", cola.popleft())

    elif len(cola) == cola.maxlen:
        print("dequeue", cola.popleft())
        
    cola.append(x)
    print("enqueue", x)
    print("En cola:", list(cola))