import runpy
from pathlib import Path

import pytest

from calculator import Calculator


def test_script_examples(capsys):
    calculator_path = Path(__file__).with_name("calculator.py")

    runpy.run_path(str(calculator_path), run_name="__main__")

    assert capsys.readouterr().out == (
        "sum: 12.0\n"
        "subtract: 8.0\n"
        "multiply: 20.0\n"
        "divide: 5.0\n"
        "divide by zero: None\n"
    )


def test_calculator_stores_operands():
    calculator = Calculator(10.0, 2.0)

    assert calculator.op1 == 10.0
    assert calculator.op2 == 2.0


@pytest.mark.parametrize(
    ("op1", "op2", "expected"),
    [
        (10.0, 2.0, 12.0),
        (-10.0, 2.0, -8.0),
        (0.0, 5.0, 5.0),
        (1.5, 2.5, 4.0),
    ],
)
def test_sum(op1, op2, expected):
    assert Calculator(op1, op2).sum() == expected


@pytest.mark.parametrize(
    ("op1", "op2", "expected"),
    [
        (10.0, 2.0, 8.0),
        (-10.0, 2.0, -12.0),
        (0.0, 5.0, -5.0),
        (1.5, 0.5, 1.0),
    ],
)
def test_subtract(op1, op2, expected):
    assert Calculator(op1, op2).subtract() == expected


@pytest.mark.parametrize(
    ("op1", "op2", "expected"),
    [
        (10.0, 2.0, 20.0),
        (-10.0, 2.0, -20.0),
        (0.0, 5.0, 0.0),
        (1.5, 2.0, 3.0),
    ],
)
def test_multiply(op1, op2, expected):
    assert Calculator(op1, op2).multiply() == expected


@pytest.mark.parametrize(
    ("op1", "op2", "expected"),
    [
        (10.0, 2.0, 5.0),
        (-10.0, 2.0, -5.0),
        (0.0, 5.0, 0.0),
        (1.5, 0.5, 3.0),
    ],
)
def test_divide(op1, op2, expected):
    assert Calculator(op1, op2).divide() == expected


@pytest.mark.parametrize("op1", [10.0, -10.0, 0.0])
def test_divide_by_zero_returns_none(op1):
    assert Calculator(op1, 0.0).divide() is None
