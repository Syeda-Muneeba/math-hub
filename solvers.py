from sympy import sympify, diff, Symbol


class PrimeChecker:
    def __init__(self, n):
        self.n = n

    def solve(self):
        if self.n < 2:
            return f"{self.n} is not prime."
        for i in range(2, int(self.n ** 0.5) + 1):
            if self.n % i == 0:
                return f"{self.n} is not prime."
        return f"{self.n} is prime."

    def explain(self):
        return "A prime number is a number greater than 1 with no divisors other than 1 and itself."


class QuadraticSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            return "No real roots."
        elif d == 0:
            root = -self.b / (2 * self.a)
            return f"One real root: {root}"
        else:
            root1 = (-self.b + d ** 0.5) / (2 * self.a)
            root2 = (-self.b - d ** 0.5) / (2 * self.a)
            return f"Two real roots: {root1} and {root2}"

    def explain(self):
        return "Solving quadratic equation ax² + bx + c = 0 using the discriminant method."


class FactorialCalculator:
    def __init__(self, n):
        self.n = n

    def solve(self):
        fact = 1
        for i in range(1, self.n + 1):
            fact *= i
        return f"Factorial of {self.n} is {fact}"

    def explain(self):
        return "Factorial of n is the product of all positive integers up to n."


class GCDSolver:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve(self):
        return f"GCD of {self.a} and {self.b} is {self.gcd(self.a, self.b)}"

    def explain(self):
        return "GCD is the greatest common divisor of two numbers."

    @staticmethod
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x


class LCMSolver:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve(self):
        gcd_value = GCDSolver.gcd(self.a, self.b)
        lcm = abs(self.a * self.b) // gcd_value
        return f"LCM of {self.a} and {self.b} is {lcm}"

    def explain(self):
        return "LCM is the least common multiple of two numbers."


class DerivativeSolver:
    def __init__(self, expression, variable='x'):
        self.expression = expression
        self.variable = variable

    def solve(self):
        try:
            expr = sympify(self.expression)
            var = Symbol(self.variable)
            derivative = diff(expr, var)
            return f"The derivative of {self.expression} with respect to {self.variable} is: {derivative}"
        except Exception as e:
            return f"Error computing derivative: {e}"

    def explain(self):
        return "Calculates the derivative of a given mathematical expression."


class FibonacciSolver:
    def __init__(self, n):
        self.n = n

    def solve(self):
        if self.n < 0:
            return "Fibonacci is not defined for negative numbers."
        elif self.n == 0:
            return "Fibonacci sequence: [0]"
        elif self.n == 1:
            return "Fibonacci sequence: [0, 1]"
        else:
            seq = [0, 1]
            for i in range(2, self.n):
                seq.append(seq[-1] + seq[-2])
            return f"Fibonacci sequence (first {self.n} terms): {seq}"

    def explain(self):
        return "Generates the Fibonacci sequence up to n terms."


class PercentageSolver:
    def __init__(self, base=None, percentage=None, value=None, value1=None, value2=None):
        # For simple percentage: base and percentage provided
        # For percentage difference: value1 and value2 provided
        self.base = base
        self.percentage = percentage
        self.value = value
        self.value1 = value1
        self.value2 = value2

    def solve(self):
        if self.base is not None and self.percentage is not None:
            # Calculate percentage of base
            result = (self.base * self.percentage) / 100
            return f"{self.percentage}% of {self.base} is {result}"
        elif self.value1 is not None and self.value2 is not None:
            # Calculate percentage difference
            try:
                diff = abs(self.value1 - self.value2)
                avg = (self.value1 + self.value2) / 2
                percent_diff = (diff / avg) * 100
                return f"Percentage difference between {self.value1} and {self.value2} is {percent_diff:.2f}%"
            except ZeroDivisionError:
                return "Cannot calculate percentage difference due to division by zero."
        else:
            return "Insufficient data to calculate percentage."

    def explain(self):
        return "Calculates either percentage of a base value or percentage difference between two values."
