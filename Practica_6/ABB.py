class NodoArbol:
    def __init__(self, clave=None, valor=None, padre=None):
        if clave is None:
            self.raiz = None
        else:
            self.clave = clave
            self.cargaUtil = valor
            self.hijoIzquierdo = None
            self.hijoDerecho = None
            self.padre = padre

    def insertar(self, clave, valor):
        if self.raiz is not None:
            self._insertar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)

    def _insertar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.hijoIzquierdo is not None:
                self._insertar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, nodoActual)

        elif clave > nodoActual.clave:
            if nodoActual.hijoDerecho is not None:
                self._insertar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, nodoActual)

        else:
            print(f"Valor repetido:{clave}")

    def imprimir_estructura(self):
        return self._estructura(self.raiz)

    def _estructura(self, nodo):
        if nodo is None:
            return ""

        izq = self._estructura(nodo.hijoIzquierdo)
        der = self._estructura(nodo.hijoDerecho)

        if izq and der:
            return f"{nodo.clave}[{izq},{der}]"
        elif izq:
            return f"{nodo.clave}[{izq}]"
        elif der:
            return f"{nodo.clave}[,{der}]"
        else:
            return f"{nodo.clave}"


    def mostrar(self, nodo=None, nivel=0):
        if nodo is None and nivel == 0:
            nodo = self.raiz

        if nodo is not None:
            print("  " * nivel + " -" + str(nodo.clave))
            self.mostrar(nodo.hijoIzquierdo, nivel + 2)
            self.mostrar(nodo.hijoDerecho, nivel + 2)


valores = [1, 13, 11, 5, 9, 10, 1, 12, 3, 6]

arbol = NodoArbol()

for v in valores:
    arbol.insertar(v, v)

print("\nÁrbol:")
arbol.mostrar()

print("Diccionario:")
print(arbol.imprimir_estructura())



