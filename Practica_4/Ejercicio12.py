#Desarrolla un programa en Python que simule una cola circular de tamaño 5 para gestionar turnos de atencion.

#El programa debe permitir:
#1. Insertar un turno en la cola.
#2. Atender un turno eliminandolo de la cola.
#3. Mostrar el turno que esta en el frente.
#4. Mostrar todos los turnos actuales en orden.
#5. Verificar si la cola esta llena o vacia.

#Ademas, realiza una prueba insertando varios turnos y mostrando como la estructura reutiliza posiciones libres.

class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_vacia(self):
        return self.frente == -1
    
    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente
    
    def encolar(self, dato):
        if self.esta_llena():
            print("La cola esta llena")
            return 
        
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final + 1) % self.capacidad

        self.cola[self.final] = dato

    def desencolar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None
        
        dato = self.cola[self.frente]

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad
        
        return dato
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.cola[self.frente]

    def mostrar(self):
        if self.esta_vacia():
            print("Cola vacia")
            return
        
        elementos = []
        i = self.frente

        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
            
        print("Cola: ", elementos)

#--------------------------------------------------
cola = ColaCircular(5)

while True:
    print("\n1. Insertar un turno en la cola")
    print("2. Atender turno elimandolo de la cola")
    print("3. Mostrar el turno que esta en el frente")
    print("4. Mostrar todos los turnos actuales en orden")
    print("5. Verificar si la cola esta llena o vacia")
    print("6. Salir")

    op = input("Opcion: ")
    if op == "1":
        turno = input("Turno: ")
        cola.encolar(turno)
    elif op == "2":
        print("Atendiendo:", cola.desencolar())
    elif op == "3":
        print("Frente:", cola.ver_frente())
    elif op == "4":
        cola.mostrar()
    elif op == "5":
        print("Vacia:", cola.esta_vacia(), "|Llena:", cola.esta_llena())
    elif op == "6":
        break
    else:
        print("Opcion no valida")