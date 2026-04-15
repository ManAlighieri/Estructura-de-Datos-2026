#1. Construcción y Análisis de un Árbol Binario de Búsqueda (ABB)
#Descripción: Dada la secuencia de números , se debe describir paso a paso cómo se insertaría cada elemento en un ABB, respetando la propiedad clave: 
# los valores menores al nodo van a la izquierda y los mayores a la derecha.

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            print(f"Insertando {clave} como raíz del árbol.")
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            print(f"Insertando {clave} a la izquierda de {nodoActual.clave}.")
            if nodoActual.tieneHijoIzquierdo():
                   self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                   print(f"Insertando {clave} como hijo izquierdo de {nodoActual.clave}.")
                   nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            print(f"Insertando {clave} a la derecha de {nodoActual.clave}.")
            if nodoActual.tieneHijoDerecho():
                   self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                   print(f"Insertando {clave} como hijo derecho de {nodoActual.clave}.")
                   nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)

    def __setitem__(self,c,v):
       self.agregar(c,v)

    def imprimir(self, nodo, nivel=0):
        if nodo:
            self.imprimir(nodo.hijoDerecho, nivel + 1)
            print(' ' * nivel + str(nodo.clave))
            self.imprimir(nodo.hijoIzquierdo, nivel + 1)

miArbol = ArbolBinarioBusqueda()

datos = [3,4,6,2]

for num in datos:
    print(f"\nInsertando {num}:")
    miArbol[num] = str(num)

print("\nArbol final:")
miArbol.imprimir(miArbol.raiz)
