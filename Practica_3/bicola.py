class Bicola:
    def __init__(self):
        self.cola = []

    def enque_head(self, elemento):
        self.cola.insert(0, elemento)

    def enque_tail(self, elemento):
        self.cola.append(elemento)

    def deque_head(self):
        if self.is_empty():
            return None
        return self.cola.pop(0)

    def deque_tail(self):
        if self.is_empty():
            return None
        return self.cola.pop(-1)

    def peek_head(self):
        return self.cola[0]

    def peek_tail(self):
        return self.cola[-1]

    def is_empty(self):
        return self.cola == []

    def size(self):
        return len(self.cola)

    def __str__(self):
        return str(self.cola)

    def retiros(self, monto):
        valor = self.deque_head()        # saca por el head
        self.enque_tail(valor - monto)   # regresa por el tail (rota)

    def depositos(self, monto):
        valor = self.deque_tail()        # saca por el tail
        self.enque_head(valor + monto)   # regresa por el head (rota)


bicola = Bicola()
bicola.enque_tail(1000)
bicola.enque_tail(1000)
bicola.enque_tail(1000)
bicola.enque_tail(1000)
bicola.enque_tail(1000)
print(bicola)

bicola.retiros(500)
bicola.retiros(400)
bicola.retiros(300)
bicola.retiros(200)
bicola.retiros(100)
print(bicola)

bicola.depositos(300)
bicola.depositos(300)
bicola.depositos(300)
bicola.depositos(300)
bicola.depositos(300)
print(bicola)

