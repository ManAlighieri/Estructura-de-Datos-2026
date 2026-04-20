class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def es_hoja(nodo):
    return nodo.izquierdo is None and nodo.derecho is None

def preorden(nodo):
    if nodo is None:
        print("None", end=",")
        return
    print(nodo.valor, end=",")
    if not es_hoja(nodo):
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

def inorden(nodo):
    if nodo is None:
        print("None", end=",")
        return
    if not es_hoja(nodo):
        inorden(nodo.izquierdo)
    print(nodo.valor, end=",")
    if not es_hoja(nodo):
        inorden(nodo.derecho)

def postorden(nodo):
    if nodo is None:
        print("None", end=",")
        return
    if not es_hoja(nodo):
        postorden(nodo.izquierdo)
        postorden(nodo.derecho)
    print(nodo.valor, end=",")

def agregar_recursivo(nodo, dato):
    if dato < nodo.valor:
        if nodo.izquierdo is None:
            nodo.izquierdo = Nodo(dato)
        else:
            agregar_recursivo(nodo.izquierdo, dato)
    else:
        if nodo.derecho is None:
            nodo.derecho = Nodo(dato)
        else:
            agregar_recursivo(nodo.derecho, dato)

valores = [1, 2, 4, 5]
raiz = Nodo(3)
for v in valores:
    agregar_recursivo(raiz, v)

print("Preorden:")
preorden(raiz)
print("\nInorden:")
inorden(raiz)
print("\nPostorden:")
postorden(raiz)


# Preorden:
# 3,1,None,2,4,None,5,
# Inorden:
# None,1,2,3,None,4,5,
# Postorden:
# None,2,1,None,5,4,3,



#         3
#       /   \
#      1     4
#     / \   /  \
#   None 2 None 5
