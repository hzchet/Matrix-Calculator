# Matrix Calculator
Данная программа является реализацией класса Matrix для вычисления различных операций над матрицами.

## Программа поддерживает следующие операции
- Сложение матриц
- Умножение матрицы на скаляр 
- Умножение матриц
- Транспонирование матрицы 
- Возведение квадратной матрицы в целую неотрицательную степень
- Решение Систем Линейных Уравнений (СЛУ) с одинаковым числом уравнений и неизвестных
- Нахождение следа квадратной матрицы

## Как использовать
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

