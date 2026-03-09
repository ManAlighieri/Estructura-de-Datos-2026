class Bicola:
    def __init__(self):
        self.cola = []

    def is_empty(self):
        return self.cola == []

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
        if self.is_empty():
            return None
        return self.cola[0]

    def peek_tail(self):
        if self.is_empty():
            return None
        return self.cola[-1]