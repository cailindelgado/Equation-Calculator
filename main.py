import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import TextBox

# import Frontend.graphing
# import Frontend.derivatives
# import Frontend.integration

""" 
i.e. "x^2 + 3x - 4 = y" --> x**2 + 3 * x - 4 = y

"""

def main():

    # Collect an equation from the user 
    equation = input("Please enter an equation: ")

    equation.replace(" ", "").split("+", -1)
    print(equation)

    
    


    # # testing setting up connection between server and logic
    # print("Hello World!")

    ''' UnComment when finished creating the connection
    # inEqn = input("please input your equation here: ")
    # rawCommand = input("would you like to derive or integrate your equation? ")

    # command = sanitize(rawCommand)
    
    # if (isValid(inEqn)):
    #     print(f"\'{inEqn}\' is invalid please enter again: ")
    
    # #identify the type of equation: i.e polynomial, trigonometric, hyperbolic etc.
    # if identify(inEqn) == 1:
    #     pass

    # if "deriv" in command: 
    #     print("poo")
    '''


if __name__ == "__main__":
    main()