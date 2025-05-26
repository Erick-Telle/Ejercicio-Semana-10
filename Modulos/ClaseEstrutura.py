class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._siguiente = None

class Cola:
    def __init__(self):
        self.frente = None  # Inicio de la cola
        self.final = None   # Final de la cola

    # Agrega un elemento a la cola
    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final._siguiente = nuevo_nodo
            self.final = nuevo_nodo

    # Elimina un elemento de la cola
    def dequeue(self):
        if self.frente is None:
            print("Error: cola vacía. No se puede eliminar.")
            return None
        eliminado = self.frente._dato
        self.frente = self.frente._siguiente
        if self.frente is None:
            self.final = None
        return eliminado

    # Método para imprimir la cola
    def imprimir(self):
        actual = self.frente
        if actual is None:
            print("La cola está vacía.")
        else:
            while actual is not None:
                print(actual._dato)
                actual = actual._siguiente


class Pila:
    def __init__(self):
        self._tope = None  # Inicia vacía

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo._siguiente = self._tope
        self._tope = nuevo_nodo
        print(f"Elemento '{dato}' insertado.")

    def pop(self):
        if self._tope is None:
            print("Error: pila vacía. No se puede eliminar.")
            return None
        eliminado = self._tope._dato
        self._tope = self._tope._siguiente
        return eliminado

    def imprimir(self):
        actual = self._tope
        while actual:
            print(actual._dato, end=" ")
            actual = actual._siguiente
        print()