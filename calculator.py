class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self) -> float:
        return self.op1 + self.op2

    def subtract(self) -> float:
        return self.op1 - self.op2

    def multiply(self) -> float:
        return self.op1 * self.op2

    def divide(self) -> float | None:
        if self.op2 == 0:
            return None
        return self.op1 / self.op2


if __name__ == "__main__":
    calculator = Calculator(10.0, 2.0)
    print("sum:", calculator.sum())
    print("subtract:", calculator.subtract())
    print("multiply:", calculator.multiply())
    print("divide:", calculator.divide())

    calculator_by_zero = Calculator(10.0, 0.0)
    print("divide by zero:", calculator_by_zero.divide())
