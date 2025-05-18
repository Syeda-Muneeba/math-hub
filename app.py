import streamlit as st

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


# Streamlit UI
st.set_page_config(page_title="Math Hub", layout="centered")
st.title("🧮 Math Hub Solver")

problem_type = st.selectbox("Choose a problem type:", ["", "Prime Check", "Quadratic Equation", "Factorial"])

result = None
explanation = None

if problem_type == "Prime Check":
    n = st.number_input("Enter a number to check:", step=1, format="%d")
    if st.button("Check Prime"):
        solver = PrimeChecker(n)
        result = solver.solve()
        explanation = solver.explain()

elif problem_type == "Quadratic Equation":
    a = st.number_input("Enter coefficient a:")
    b = st.number_input("Enter coefficient b:")
    c = st.number_input("Enter coefficient c:")
    if st.button("Solve Quadratic"):
        solver = QuadraticSolver(a, b, c)
        result = solver.solve()
        explanation = solver.explain()

elif problem_type == "Factorial":
    n = st.number_input("Enter a non-negative integer:", step=1, format="%d")
    if n < 0:
        st.error("Factorial is not defined for negative numbers.")
    elif st.button("Calculate Factorial"):
        solver = FactorialCalculator(n)
        result = solver.solve()
        explanation = solver.explain()

# Display results
if result:
    st.success(result)
if explanation:
    st.info(explanation)

# Optional: placeholder for future "History" section
with st.expander("🕒 View History (coming soon)"):
    st.write("This section will show past calculations.")
