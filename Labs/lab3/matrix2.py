import random
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result

    def set_value(self, row, col,value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
           
            self.data[row][col] = value
        else:
            raise ValueError("Row or column index out of bounds.")

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise ValueError("Row or column index out of bounds.")

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(i, j, self.get_value(i, j) + other.get_value(i, j))
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                product = 0
                for k in range(self.cols):
                    product += self.get_value(i, k) * other.get_value(k, j)
                result.set_value(i, j, product)
        return result

    def negate(self):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(i, j, -self.get_value(i, j))
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                result.set_value(i, j, self.get_value(j, i))
        return result

# Example usage:
matrix1 = Matrix(2, 2)
matrix1.set_value(0, 0, 1)
matrix1.set_value(0, 1, 2)
matrix1.set_value(1, 0, 3)
matrix1.set_value(1, 1, 4)

matrix2 = Matrix(2, 2)
matrix2.set_value(0, 0, 7)
matrix2.set_value(0, 1, 6)
matrix2.set_value(1, 0, 7)
matrix2.set_value(1, 1, 8)

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

result = matrix1.add(matrix2)
print("Matrix 1 + Matrix 2:")
print(result)

result = matrix1.multiply(matrix2)
print("Matrix 1 * Matrix 2:")
print(result)

result = matrix1.negate()
print("Negation of Matrix 1:")
print(result)

result = matrix1.transpose()
print("Transpose of Matrix 1:")
print(result)
