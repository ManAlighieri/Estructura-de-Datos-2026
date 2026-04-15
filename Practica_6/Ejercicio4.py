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