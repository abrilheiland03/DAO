from funciones import cargarLineas, promedio, mayores, pares

def main():
    # Solicitar al usuario que ingrese el nombre del archivo
    lista_numeros = cargarLineas("numeros.txt")

    if lista_numeros:
        #1. Calcular el promedio
        prom = promedio(lista_numeros)

        #2. Cantidad de numeros mayores al promedio
        mayores_al_promedio = mayores(lista_numeros, prom)
        cantidad_mayores = len(mayores_al_promedio)

        #3. Pares
        numeros_pares = pares(lista_numeros)

        #4. Mostrar resultados
        print(f"Promedio: {prom}")
        print(f"Cantidad de números mayores al promedio: {cantidad_mayores}")
        print(f"Números pares: ")
        for num in numeros_pares:
                print(num)
    else:
        print("La lista de números está vacía.")


if __name__ == "__main__":
    main()