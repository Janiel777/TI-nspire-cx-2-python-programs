class Fraction:
    def __init__(self, string):
        if "/" in string:
            self.numerator, self.denominator = map(int, string.split("/"))
        else:
            self.numerator = int(string)
            self.denominator = 1

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        result = Fraction("{0}/{1}".format(num, den))
        result.simplify()
        return result

    def __sub__(self, other):
        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator
        result = Fraction("{0}/{1}".format(num, den))
        result.simplify()
        return result

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        result = Fraction("{0}/{1}".format(num, den))
        result.simplify()
        return result

    def __truediv__(self, other):
        if other.denominator == 0:
            raise ZeroDivisionError("division by zero")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        result = Fraction("{0}/{1}".format(num, den))
        result.simplify()
        return result

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return "{0}/{1}".format(self.numerator, self.denominator)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
def printMatrix(matrix):
    for row in matrix:
        print([str(x) for x in row])
    print()
    
def gauss_jordan(matrix, m):
    try:
        for i in range(m):
            # Dividir la fila por el pivote
            pivot = matrix[i][i]
            for j in range(m + 1):
                matrix[i][j] = matrix[i][j].__truediv__(pivot)
            print("R{0}/{1}".format(i+1,pivot))
            printMatrix(matrix)
            
            # Hacer ceros en las filas debajo del pivote
            for k in range(i + 1, m):
                factor = matrix[k][i]
                for j in range(i, m + 1):
                    matrix[k][j] = matrix[k][j].__sub__(factor.__mul__(matrix[i][j]))
                print("R{0} - R{1}*{2}".format(k+1, i+1, factor))
                printMatrix(matrix)
        
        # Hacer ceros en las filas arriba del pivote
        for i in range(m - 1, -1, -1):
            for k in range(i - 1, -1, -1):
                factor = matrix[k][i]
                for j in range(m + 1):
                    matrix[k][j] = matrix[k][j].__sub__(factor.__mul__(matrix[i][j]))
                print("R{0} - R{1}*{2}".format(k+1, i+1, factor))
                printMatrix(matrix)
        
        return [row[-1] for row in matrix]
    except ZeroDivisionError as e:
        print("Error:", e)

# Prueba 1

m = int(input("Enter the number of equations: "))
matrix = []
for i in range(m):
    matrix.append([Fraction(x) for x in input("Enter row {} (elements separated by spaces): ").strip().split()])
    
solution = gauss_jordan(matrix, m)
print("The solution is: ", [str(x) for x in solution])
