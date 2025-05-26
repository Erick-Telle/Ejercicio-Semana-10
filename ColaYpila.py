from Modulos.ClaseEstrutura import Cola,Pila

# Principal
if __name__ == "__main__":
    mi_pila = Pila()
    mi_cola = Cola()

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for numero in numeros:
        if numero % 2 == 0:  # Número par
            mi_cola.enqueue(numero)
        else:  # Número impar
            mi_pila.push(numero)

    print("Números en la cola (pares):")
    mi_cola.imprimir()

    print("Números en la pila (impares):")
    mi_pila.imprimir()
