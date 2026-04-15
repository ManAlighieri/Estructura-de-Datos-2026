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