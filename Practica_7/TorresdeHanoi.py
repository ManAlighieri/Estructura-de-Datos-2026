def moverTorre(altura, origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1, origen, intermedio, destino)
        moverDisco(altura, origen, destino)  
        moverTorre(altura-1, intermedio, destino, origen)

def moverDisco(disco, desde, hacia):
    print(f"Mover disco {disco} de {desde} a {hacia}")

moverTorre(5, "A", "B", "C")