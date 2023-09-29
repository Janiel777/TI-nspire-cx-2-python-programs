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
    
    
    
def get_matrix(n):
    matrix = []
    for i in range(n):
        row = input("Enter row {} (elements separated by spaces): ".format(i+1)).split()
        matrix.append([Fraction(element) for element in row])
    return matrix
    
def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(element) for element in row]))
    print()
    
def inverse_matrix(matrix):
    n = len(matrix)
    augmented = []
    for i in range(n):
        row = []
        for j in range(n * 2):
            if j < n:
                row.append(Fraction(str(matrix[i][j])))
            else:
                if i == j - n:
                    row.append(Fraction("1"))
                else:
                    row.append(Fraction("0"))
        augmented.append(row)

    for i in range(n):
        pivot = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] = augmented[i][j].__truediv__(pivot)
        print("R{0}/{1}".format(i+1,pivot))
        print_matrix(augmented)
        for k in range(n):
            if k == i:
                continue
            scale = augmented[k][i]
            for j in range(2 * n):
                augmented[k][j] = augmented[k][j].__sub__(scale.__mul__(augmented[i][j]))
            print("R{0} - R{1}*{2}".format(k+1, i+1, scale))
            print_matrix(augmented)

    inverse = []
    for i in range(n):
        row = []
        for j in range(n, n * 2):
            row.append(augmented[i][j])
        inverse.append(row)
    return inverse



n = int(input("Enter the size of the square matrix: "))
matrix = get_matrix(n)
print("The original matrix is:")
print_matrix(matrix)

inverse = inverse_matrix(matrix)
print("The inverse of the matrix is:")
print_matrix(inverse)
