def multiplicar_matrices(A, B):
    # obtener dimensiones
    filas_A = len(A)
    cols_A = len(A[0])
    filas_B = len(B)
    cols_B = len(B[0])

    # checar si se pueden multiplicar A y B
    if cols_A != filas_B:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

    # Inicializar una matriz vacía con ceros
    matriz_resultado = []
    for _ in range(filas_A):
        fila = []
        for _ in range(cols_B):
            fila.append(0)
        matriz_resultado.append(fila)

    print(matriz_resultado)

    count = 0

    # realizar multiplicación
    for i in range(filas_A):
        print("este es i: ", i)
        for j in range(cols_B):
            print("este es j: ", j)
            for k in range(cols_A):
                print("este es k: ", k)
                matriz_resultado[i][j] += A[i][k] * B[k][j]
                count += 1
                print("--------------------")
                
                print("!!!!!iteracion!!!!!: ", count)
                print("este es el vector de A: ", A[i][k])
                print("esta es el vector de B: ", B[k][j])
                print(matriz_resultado)
                print(matriz_resultado[i][j])
                print("--------------------")

    return matriz_resultado

# Ejemplo
A = [
    [1, 2, 3],
    [4, 5, 6],
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
C = multiplicar_matrices(A, B)
print(C)