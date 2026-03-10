from collections import deque

cola = deque(maxlen=3)
limite = 10
tiempo = [0, 2, 4, 6, 12]

for x in tiempo:
    print("\nLlega", x)
    if cola and x - cola[0] >= limite:
        while cola:
            print("Se retiro", cola.popleft())
        print("Se agrega", x)
        cola.append(x)

    elif len(cola) < cola.maxlen:
        print("Se agrega", x)
        cola.append(x)

print("En cola:", cola)
print("Lista:", list(cola))