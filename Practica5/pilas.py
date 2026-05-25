class Pila:
    def _init_(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def peek(self):
        return self.elementos[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.elementos) == 0