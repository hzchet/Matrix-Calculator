from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, rows):
        self.rows = deepcopy(rows)

    def __str__(self):
        tempList = []
        for row in self.rows:
            tempList.append('\t'.join(map(str, row)))
        return '\n'.join(tempList)

    def size(self):
        return len(self.rows), len(self.rows[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise Exception('Matrices must be of the same size.')
        result = []
        temp = []
        for i in range(len(self.rows)):
            temp = []
            for j in range(len(self.rows[i])):
                temp.append(self.rows[i][j] + other.rows[i][j])
            result.append(temp)
        return Matrix(result)

    def __sub__(self, other):
        return self + (-1 * other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for row in self.rows:
                temp = []
                for num in row:
                    temp.append(num * other)
                result.append(temp)
            return Matrix(result)

        elif isinstance(other, Matrix):
            if other.size()[0] != self.size()[1]:
                raise Exception('The number of columns in the first matrix '
                                'should be equal to the number of rows in the second.')

            rows = self.size()[0]
            cols = other.size()[1]
            result = [0] * rows
            for i in range(rows):
                result[i] = [0] * cols
            temp = Matrix.transposed(other)
            for i in range(rows):
                for j in range(cols):
                    result[i][j] = sum(
                        map(
                            lambda x: x[0] * x[1],
                            zip(
                                self.rows[i], temp.rows[j]
                            )
                        )
                    )

            return Matrix(result)

        else:
            raise Exception('You can only multiply matrix by another matrix or a number.')

    __rmul__ = __mul__

    def transpose(self):
        result = list(zip(*self.rows))
        self.rows = result
        return Matrix(result)

    def transposed(self):
        result = list(zip(*self.rows))
        return Matrix(result)


class SquareMatrix(Matrix):
    def __pow__(self, power, modulo=None):
        if power == 0:
            result = [0] * self.size()[0]
            for i in range(self.size()[0]):
                result[i] = [0] * self.size()[0]
            for i in range(self.size()[0]):
                for j in range(self.size()[0]):
                    if i == j:
                        result[i][j] = 1
                    else:
                        result[i][j] = 0
            return SquareMatrix(result)
        else:
            if power % 2 == 0:
                return pow(SquareMatrix((self * self).rows), power // 2)
            else:
                return self * pow(self, power - 1)

    def solve(self, free_terms):
        if len(free_terms) != len(self.rows):
            raise Exception('The number of left and right sides of the equations is different.')
        if len(free_terms) == self.size()[0] == self.size()[1]:
            n = self.size()[0]
            for i in range(n):
                self.rows[i].append(free_terms[i])
            a = self.rows

            # Прямой ход метода Гаусса
            for j in range(n):
                for i in range(j, n):
                    if a[i][j] != 0:
                        temp = a[j][j]
                        a[j][j] = a[i][j]
                        a[i][j] = temp
                        break
                else:
                    raise Exception('The system of linear equations has no solution.')
                for i in range(j + 1, n):
                    d = a[i][j]
                    for x in range(j, n + 1):
                        a[i][x] -= a[j][x] * d / a[j][j]

            # Обратный ход метода Гаусса
            for i in range(n - 1, -1, -1):
                d = a[i][i]
                for j in range(i, n + 1):
                    a[i][j] /= d
                b = deepcopy(a)

                for x in range(i - 1, -1, -1):
                    for j in range(i, n + 1):
                        a[x][j] -= b[i][j] * b[x][i]

            ans = []
            for i in range(n):
                ans.append(a[i][n])
            return ans

    def trace(self):
        return sum([self.rows[i][i] for i in range(len(self.rows))])


if __name__ == '__main__':
    exec(stdin.read())
