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

#2. Modelado de un Sistema de Archivos (Árbol N-ario)
#Descripción: Se propone diseñar la jerarquía de directorios para un proyecto de software. 
# La raíz es la carpeta Proyecto. Dentro de ella, existen tres carpetas: src, docs y assets.

# En src hay dos archivos: main.py y utils.py.
# En docs hay una subcarpeta llamada v1 que contiene el archivo manual.pdf.
# En assets hay tres imágenes. Tarea: Describe esta estructura identificando formalmente qué nodos actúan como nodos internos 
# (carpetas) y cuáles como nodos hoja (archivos), justificando por qué este es un ejemplo de Árbol N-ario debido a su flexibilidad en el grado de los nodos.

class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.hijos = []  # lista de referencias a nodos hijos

  def agregar_hijo(self, nodo_hijo):
    if nodo_hijo is None:
      return
    self.hijos.append(nodo_hijo)

proyecto = Nodo("Proyecto")

src = Nodo("src")   
docs = Nodo("docs")
assets = Nodo("assets")

proyecto.agregar_hijo(src)
proyecto.agregar_hijo(docs)
proyecto.agregar_hijo(assets)

src.agregar_hijo(Nodo("main.py"))
src.agregar_hijo(Nodo("utils.py"))

v1 = Nodo("v1")
docs.agregar_hijo(v1)
v1.agregar_hijo(Nodo("manual.pdf"))

assets.agregar_hijo(Nodo("imagen1.png"))
assets.agregar_hijo(Nodo("imagen2.png"))
assets.agregar_hijo(Nodo("imagen3.png"))

#3. Compresión de Datos con el Algoritmo de Huffman
#Descripción: Supongamos que tenemos un mensaje donde la letra "E" aparece 50 veces, la "A" 30 veces y la "Z" solo 2 veces. 
# Tarea: Describe el proceso lógico para construir un Árbol de Huffman con estos datos. 
# Debes explicar por qué los caracteres más frecuentes ("E" y "A") deben situarse más cerca de la raíz y 
# cómo se asignarían los códigos binarios (0 para la izquierda, 1 para la derecha) para lograr que el archivo 
# resultante ocupe menos espacio.

# Código Huffman en Python

freq = {
    'E': 50,
    'A': 30,
    'Z': 2
}

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    
    (l, r) = node.children()
    d = dict()

    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

nodes = sorted(freq.items(), key=lambda x: x[1])


while len(nodes) > 1:
    (key1, c1) = nodes[0]
    (key2, c2) = nodes[1]

    nodes = nodes[2:]

    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for char, _ in sorted(freq.items()):
    print(f"{char} | {huffmanCode[char]}")

#4. Implementación de Autocompletado con un Trie
#Descripción: Imagina que estás diseñando el buscador de una tienda en línea y quieres sugerir palabras que comiencen con "cam".
# En tu diccionario tienes las palabras: "cama", "camino", "campo" y "carro". Tarea: Describe cómo se estructuraría un Trie 
# (árbol de prefijos) para estas palabras. Debes detallar cómo los nodos comparten la raíz común 'c', 'a' y 'm', y cómo 
# el sistema navegaría por el árbol para listar todos los descendientes del nodo 'm' de forma eficiente en tiempo O(m), 
# superando la eficiencia de una búsqueda lineal.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        self.root = TrieNode()

    def formTrie(self, keys):


        for key in keys:
            self.insert(key) 

    def insert(self, key):

 
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestionsRec(self, node, word):

        if node.last:
            print(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        node = self.root

        for a in key:
            if not node.children.get(a):
                return 0
            node = node.children[a]

        if not node.children:
            return -1

        self.suggestionsRec(node, key)
        return 1


keys = ["cama", "camino", "campo", "carro"]  
key = "cam"  


t = Trie()


t.formTrie(keys)

print("Sugerencias para 'cam':")
comp = t.printAutoSuggestions(key)

if comp == -1:
    print("No hay mas palabras con este prefijo\n")
elif comp == 0:
    print("No se encontró ninguna palabra con este prefijo\n")

#5. Análisis Sintáctico de Expresiones (AST)
#Descripción: Tomando como base la expresión matemática (8 + 4) * 2. 
# Tarea: Describe cómo un compilador representaría esta operación mediante un Árbol de Sintaxis Abstracta (AST). 
# Debes identificar cuál sería el nodo raíz (la operación de mayor jerarquía tras evaluar los paréntesis), 
# cuáles serían los nodos internos y cuáles serían las hojas (los literales o números). 
# Explica cómo esta estructura permite al compilador respetar la precedencia de los operadores.

class NodoAST:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

    def es_hoja(self):
        return self.izq is None and self.der is None

    def evaluar(self):
        if self.es_hoja():
            return int(self.valor)
        izq = self.izq.evaluar()
        der = self.der.evaluar()
        ops = {"+": izq + der, "-": izq - der,
               "*": izq * der, "/": izq / der}
        return ops[self.valor]

    def imprimir(self, nivel=0, prefijo=""):
        tipo = "[hoja]" if self.es_hoja() else "[op]  "
        print(prefijo + tipo + " " + str(self.valor))
        if self.izq: self.izq.imprimir(nivel+1, prefijo + "  ├─ ")
        if self.der: self.der.imprimir(nivel+1, prefijo + "  └─ ")

def construir_ast_simple(expr):
    "Parser básico para expresiones con paréntesis."
    expr = expr.replace(" ", "")
    def parse(s):
        if not s:
            return NodoAST("")
        if s[0] == "(" and s[-1] == ")":
            s = s[1:-1]
        for op in ("+-", "*/"):
            depth = 0
            for i in range(len(s)-1, -1, -1):
                if s[i] == ")": depth += 1
                elif s[i] == "(": depth -= 1
                elif depth == 0 and s[i] in op:
                    nodo     = NodoAST(s[i])
                    nodo.izq = parse(s[:i])
                    nodo.der = parse(s[i+1:])
                    return nodo
        return NodoAST(s)
    return parse(expr)

expresiones = ["(8 + 4) * 2", "10 + 3 * 5", "(6 - 2) * (3 + 1)"]
for expr in expresiones:
    ast = construir_ast_simple(expr)
    print(f"\nExpresión: {expr} = {ast.evaluar():.0f}")
    print("AST:")
    ast.imprimir()

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
