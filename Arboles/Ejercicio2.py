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