from ClaseEstrutura import Cola, Pila

def procesar_cola_y_pila(cola):
    pila = Pila()
    contador = 0
    
    while not cola.is_empty():
        elemento = cola.dequeue()
        if contador % 2 == 0:  # Posiciones pares
            cola.enqueue(elemento)
        else:  # Posiciones impares
            pila.push(elemento)
        contador += 1

    return pila