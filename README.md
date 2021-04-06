# Matrix Calculator
Данная программа является реализацией класса Matrix для вычисления различных операций над матрицами.

## Программа поддерживает следующие операции
Класс `Matrix`:
  - Сложение матриц
  - Умножение матрицы на скаляр 
  - Умножение матриц
  - Транспонирование матрицы

Класс `Square Matrix`: 
- Возведение квадратной матрицы в целую неотрицательную степень
- Решение Систем Линейных Уравнений (СЛУ) с одинаковым числом уравнений и неизвестных
- Нахождение следа квадратной матрицы

## Инициализация
Для создания матрицы нужно использовать массив массивов (массив строк) как в библиотеке numpy. К примеру, код
```python
E = Matrix([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
A = Matrix([[1, 2, 3]])
B = Matrix([[4], [5], [6]])
```
создаст следующие матрицы

![](https://github.com/hzchet/Matrix-Calculator/blob/main/Matrix_example1.png?raw=true)

### Использование операций
Можно складывать 2 матрицы одинакового размера. К примеру
```python
A = Matrix([[1, 2, 3],
            [4, 5, 6]])
B = Matrix([[-1, 2, -3],
            [4, -5, 6]])
print(A + B)
```
выведет
```python
0	4	0
8	0	12
```
Умножать матрицы друг на друга или на скаляр:
```python
A = Matrix([[1, 2, 3],
            [4, 5, 6]])
B = Matrix([[1, 1],
            [1, 1],
            [0, 0]])
print(A * B)
```
```python
3	3
9	9
```
Транспонировать матрицу
```python
A = Matrix([[1, 2, 3],
            [4, 5, 6]])
print(A.transposed())
```
```python
1	4
2	5
3	6
```
### SquareMatrix
Для применения специфичных для квадратных матриц операций можно испольлзовать класс `SquareMatrix`. Данный класс является наследником класса `Matrix` и поддерживает все операции применимые к матрицам произвольного размера.

Можно возводить квадратные матрицы в целую неотрицательную степень:
```python
M = SquareMatrix([[1, 1, 1],
                  [0, 0, 0],
                  [1, 0, 0]])
print(M ** 2)
```
```python
2	1	1
0	0	0
1	1	1
```
Умеет решать СЛУ с одинаковым количеством переменных и уравнений. К примеру, рассмотрим следующую систему линейных уравнений
![](https://github.com/hzchet/Matrix-Calculator/blob/main/Linear-equation-example.png?raw=True)
и запишем ее в матричной форме
![](https://github.com/hzchet/Matrix-Calculator/blob/main/Linear-equation-Matirx-form-example..png?raw=True)
Для решения этогй системы можем использовать метод `solve`:
```python
A = SquareMatrix([[2, 3, -1],
                  [1, -2, 1],
                  [1, 0, 2]])
b = [9, 3, 2]
print(A.solve(b))
```
```python
[4.0, 0.0, -1.0]
```
И дополнительно, есть возможность нахождения следа квадратной матрицы (т.е. сумма диагональных элементов):
```python
A = SquareMatrix([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(A.trace())
```
```python
15
```
