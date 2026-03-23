Dulces = [12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75]

class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if not self.is_empty():
            return self.elementos.pop(0)

    def is_empty(self):
        return len(self.elementos) == 0

    def size(self):
        return len(self.elementos)

    def __str__(self):
        return str(self.elementos)

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def peek(self):
        return self.elementos[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.elementos) == 0

    def __str__(self):
        return str(self.elementos)

cola = Cola()
for x in sorted(Dulces):
    cola.enqueue(x)

pila = Pila()
while not cola.is_empty():
    pila.push(cola.dequeue())

print("Pila ordenada:", pila)