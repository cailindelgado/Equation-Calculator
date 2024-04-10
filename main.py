import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import TextBox

import functions
import graphing
import derivatives
import integration

""" 
i.e. "x^2 + 3x - 4 = y" --> x**2 + 3 * x - 4 = y

"""

def sanitize(cmd: str) -> str:
    return cmd.strip().lower().replace(" ", "")

def isValid(equation: str) -> bool:
    for char in equation:
        if char in "`~!@#$$%&_+-=[]\;',./<>?:":
            return False
    return True

"""
Identifies the type of equation based off of the input string.

>>> identify("3x^2 + 4y")
polynomial
"""
def identify(euqation: str) -> int:
    #polynomial, exponential, logarithmic, 
    pass
    


def main():
    print()
    inEqn = input("please input your equation here: ")
    rawCommand = input("would you like to derive or integrate your equation? ")

    command = sanitize(rawCommand)
    
    if (isValid(inEqn)):
        print(f"\'{inEqn}\' is invalid please enter again: ")
    
    #identify the type of equation: i.e polynomial, trigonometric, hyperbolic etc.
    if identify(inEqn) == 1:
        pass

    if "deriv" in command: 
        print("poo")


if __name__ == "__main__":
    main()