# Multiplicación de Matrices Paso a Paso en Python (Vanilla)

Este proyecto contiene un script en Python puro que realiza la **multiplicación de matrices**, pero con un enfoque educativo: **desarmar y mostrar paso a paso cómo funciona cada ciclo** dentro del algoritmo. La intención es entender de forma orgánica y detallada cómo se lleva a cabo esta operación, sin usar librerías externas como NumPy.

---

## 🧠 Propósito

Muchas veces usamos código que ya está optimizado o encapsulado en librerías, lo cual resuelve el problema, pero **no necesariamente nos enseña qué está pasando**.

Este código tiene como objetivo:

- Comprender **cómo se multiplican matrices manualmente**.
- Observar **cómo interactúan los ciclos anidados**.
- Imprimir información clave en cada paso para ver cómo se construye la matriz final.
- Desarrollar **intuición** sobre cómo funcionan los índices y las posiciones en las matrices.

---

## 📌 ¿Qué hace el código?

1. Verifica que las matrices se pueden multiplicar (es decir, que el número de columnas de A sea igual al número de filas de B).
2. Inicializa una matriz vacía (`matriz_resultado`) con ceros, con las dimensiones adecuadas.
3. Utiliza tres ciclos `for` anidados para realizar la multiplicación:
   - `i`: recorre las **filas de A**.
   - `j`: recorre las **columnas de B**.
   - `k`: recorre los elementos de la fila de A y la columna de B para realizar la **multiplicación y suma acumulada**.

En cada iteración, el código imprime:

- El número de iteración.
- El valor que toma de `A[i][k]` y de `B[k][j]`.
- El estado actual de la `matriz_resultado`.

Esto permite **ver visualmente cómo se construye cada celda** de la matriz final.

---

## 💻 Ejemplo de entrada

```python
A = [
    [1, 2, 3],
    [4, 5, 6],
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
```
## 🧪 Salida esperada
Durante la ejecución se imprimen detalles de cada paso y, al final, la matriz resultante:
```
[[58, 64],
 [139, 154]]
```
## 🔁 ¿Por qué hay 3 ciclos?
El primer ciclo (i) elige qué fila de A vamos a usar.

El segundo ciclo (j) elige qué columna de B vamos a combinar con esa fila.

El tercer ciclo (k) recorre cada elemento de la fila y columna seleccionadas y realiza:

```
matriz_resultado[i][j] += A[i][k] * B[k][j]
```

## 🛠 Requisitos
Solo necesitas Python 3. No se usan paquetes externos.

Ejecuta con:
```
python3 main.py
```