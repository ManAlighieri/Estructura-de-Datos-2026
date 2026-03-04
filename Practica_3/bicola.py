def enque(lista, elemento):
    lista.append(elemento)
    
def  deque_head(lista,lista2):
    enque(lista2,lista[0])
    lista.pop(0)

def  deque_tail(lista,lista2):
    enque(lista2,lista[-1])
    lista.pop(-1)

def peek(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False
    
def size(lista):
    return len(lista)

def retiros(lista, lista2):
    r = lista[0] - lista2[0]
    deque_head(lista, lista2)
    enque(lista, r)

def depositos(lista, lista2):
    d = lista[-1] + lista2[0]
    deque_tail(lista, lista2)
    lista.insert(0, d)

saldos = []
retiro = []
deposito = []    

enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
print(saldos)

retiro = [500]
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
print(saldos)

deposito = [300]
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
print(saldos)