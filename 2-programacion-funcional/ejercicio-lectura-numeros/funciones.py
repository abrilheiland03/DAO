def cargarLineas(nombreArchivo: str) -> list[str]:
    """Carga un archivo y devuelve un conjunto de líneas limpias en minúsculas."""
    with open(nombreArchivo, "r", encoding="utf-8") as f:
        return {float(line.strip()) for line in f}

def promedio(numeros: list[float]) -> float:
    """Calcula el promedio de una lista de números."""
    return sum(numeros) / len(numeros) if numeros else 0.0

def pares(numeros: list[int]) -> set[int]:
    """Devuelve una lista, sin duplciados, con los números pares de la lista dada."""
    return {num for num in numeros if num % 2 == 0}

def mayores (numeros: list[int], promedio) -> set[int]:
    """Devuelve  lista sin duplicados con los números mayores que el umbral dado."""
    return {num for num in numeros if num > promedio}