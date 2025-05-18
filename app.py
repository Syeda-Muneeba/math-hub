from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change to a strong secret key


# Solver classes
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
        return "Solving quadratic equation ax² + bx + c = 0 using discriminant method."


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


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    explanation = None
    problem_type = None

    if request.method == 'POST':
        problem_type = request.form.get('problem_type')

        try:
            if problem_type == 'prime':
                n = int(request.form.get('prime_number'))
                solver = PrimeChecker(n)
            elif problem_type == 'quadratic':
                a = float(request.form.get('a'))
                b = float(request.form.get('b'))
                c = float(request.form.get('c'))
                solver = QuadraticSolver(a, b, c)
            elif problem_type == 'factorial':
                n = int(request.form.get('factorial_number'))
                if n < 0:
                    flash("Factorial is not defined for negative numbers.", "danger")
                    return redirect(url_for('index'))
                solver = FactorialCalculator(n)
            else:
                flash("Please select a valid problem type.", "danger")
                return redirect(url_for('index'))

            result = solver.solve()
            explanation = solver.explain()

        except Exception:
            flash("Invalid input. Please check your values.", "danger")
            return redirect(url_for('index'))

    return render_template('index.html', result=result, explanation=explanation, problem_type=problem_type)


@app.route('/history')
def history():
    # Placeholder page for History
    return render_template('history.html')


if __name__ == '__main__':
    app.run(debug=True)
