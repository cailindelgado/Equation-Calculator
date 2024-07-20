import pytest
import logic_handler as lh


def test_equation_handler_1():
    with pytest.raises(lh.ParseError):
        lh.equationHandler(")/(")


# print(equationHandler(")/(") + "\n")
# print(equationHandler("4x + (3x^2)^2 + 1") + "\n")
# print(equationHandler("(6x^3)/-9x+4") + "\n")
# print(equationHandler("(2x+4)-3x+4x^2-3(12x-3)+4/(3+2x)") + "\n")
# print(equationHandler("(2x+4)+(12x-3)+(4x^2)/(3+2x)") + "\n")
