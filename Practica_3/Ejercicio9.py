def enque(lista, elemento):
    lista.append(elemento)
    
def  deque(lista,lista2):
    enque(lista2,lista[0])
    lista.pop(0)

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
    deque(lista, lista2)
    enque(lista, r)

def depositos(lista, lista2):
    d = lista[0] + lista2[0]
    deque(lista, lista2)
    enque(lista, d)

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


