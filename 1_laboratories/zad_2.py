class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Matrix(self.a + other.a,
                      self.b + other.b,
                      self.c + other.c,
                      self.d + other.d)

    def __mul__(self, other):
        return Matrix(self.a * other.a + self.b * other.c,
                      self.a * other.b + self.b * other.d,
                      self.c * other.a + self.d * other.c,
                      self.c * other.b + self.d * other.d
                      )

    def __str__(self):
        return f"{self.a, self.b}\n{self.c, self.d}"

    def __repr__(self):
        return f"Matrix result:\n{self.a, self.b}\n{self.c, self.d}"


matrix1 = Matrix(1, 1, 1, 1)
matrix2 = Matrix(2, 2, 2, 2)

matrix3 = matrix1 + matrix2
matrix4 = matrix1 * matrix2

print (f"Matrix number 1: \n{matrix1}")
print (f"Matrix number 2: \n{matrix2}")
print(f"Sum of matrix1 and matrix2: \n{matrix3}")
print(f"Mult of matrix1 and matrix2: \n{matrix4}")
print(repr(matrix4))