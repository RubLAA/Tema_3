from matriz import Matriz

if __name__ == "__main__":
    # Caso 1: Matriz 3x3 diagonal (determinante = 2*3*4 = 24)
    matriz_diagonal = [
        [2, 0, 0],
        [0, 3, 0],
        [0, 0, 4]
    ]
    m1 = Matriz(matriz_diagonal)
    print(f"Diagonal 3x3 | Iterativo: {m1.determinante_iterativo()} | Recursivo: {m1.determinante_recursivo()}")
    
    # Caso 2: Matriz 3x3 no diagonal (determinante = -2)
    matriz_general = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = Matriz(matriz_general)
    print(f"General 3x3  | Iterativo: {m2.determinante_iterativo()} | Recursivo: {m2.determinante_recursivo()}")
    
    # Caso 3: Matriz 2x2 (solo recursivo)
    matriz_2x2 = [
        [5, 3],
        [2, 4]
    ]
    m3 = Matriz(matriz_2x2)
    print(f"Matriz 2x2   | Recursivo: {m3.determinante_recursivo()}")  # 5*4 - 3*2 = 14

    # Caso 4: Matriz 1x1 (solo recursivo)
    matriz_1x1 = [[10]]
    m4 = Matriz(matriz_1x1)
    print(f"Matriz 1x1   | Recursivo: {m4.determinante_recursivo()}")  # 10

    # Caso de error controlado (matriz no cuadrada)
    try:
        matriz_no_cuadrada = [[1, 2], [3]]
        m5 = Matriz(matriz_no_cuadrada)
    except ValueError as e:
        print(f"Error controlado: {e}")