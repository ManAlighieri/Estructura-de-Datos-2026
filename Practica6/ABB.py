class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre


def abb_diccionario(secuencia):
    vistos = {}
    indice = {}
    raiz = None

    def insertar(nodo, clave):
        if nodo is None:
            nuevo = NodoArbol(clave, clave)
            indice[clave] = nuevo
            return nuevo

        if clave < nodo.clave:
            nodo.hijoIzquierdo = insertar(nodo.hijoIzquierdo, clave)
            nodo.hijoIzquierdo.padre = nodo
        elif clave > nodo.clave:
            nodo.hijoDerecho = insertar(nodo.hijoDerecho, clave)
            nodo.hijoDerecho.padre = nodo

        return nodo

    for num in secuencia:
        if num in vistos:
            continue
        vistos[num] = True
        raiz = insertar(raiz, num)

    dic_final = {}
    for clave, nodo in indice.items():
        izq = nodo.hijoIzquierdo.clave if nodo.hijoIzquierdo else None
        der = nodo.hijoDerecho.clave if nodo.hijoDerecho else None
        dic_final[clave] = (izq, der)

    return dic_final


# Ejemplo
secuencia = [1, 13, 11, 5, 9, 10, 1, 12, 3, 6]
print(abb_diccionario(secuencia))



