import matplotlib.pyplot as plt
import numpy as np
import re                                   # using the Regex module for interpreting an equation

from matplotlib.widgets import TextBox

# custom exception/error that is raised when a problem occurs when parsing the given equation
class ParseError(Exception):
    pass

def equationHandler(eqn: str) -> str:
    try:
        eqnBits = eqnParser(eqn.strip())
        eqn = ""
        for bit in eqnBits:
            eqn += bit
    except ParseError as e:
        eqn = str(e)
    return eqn

    # testing setting up connection between server and logic
    print("Hello World!")

def replacement(eqn: str) -> list[str]:
    eqn.strip().replace(" ", "")

    OBpositions = [] # list that contains positions of ({[
    CBpositions = [] # list that contains positions of )}]
    
    for pos, char in enumerate(eqn):
        if char in "({[]})":
            pass 

    print(OBpositions)
    print(CBpositions)

    return eqn.split() # fix this 


def eqnParser(eqn: str) -> list[str]:
    eqn.strip().replace(" ", "")
    #to parse the given equation: "(2x+4)-3x+4x^2-(12x-3)+4/(3+2x)"
    # 1. check for brackets take note of each starting bracket and ending bracket
    bracketPositions = []
    OBpositions = [] # list that contains positions of ({[
    CBpositions = [] # list that contains positions of )}]
    for pos, char in enumerate(eqn):
        if char in "({[]})":
            bracketPositions.append(pos)
            OBpositions.append(pos) if char in "({[" else CBpositions.append(pos)

        elif char in "~!@#$%&`_=\\|'\":;?<>,.":
            raise ParseError(f"Invalid Character: {char}")

    if len(OBpositions) != len(CBpositions):
        raise ParseError("Un-partnered bracket")
    
    OBpositions = eqnParserHelper(OBpositions, eqn, True)
    CBpositions = eqnParserHelper(CBpositions, eqn, False)
    
    
    temp = OBpositions.copy()
    for pos in temp:
        # if the characters beside each open bracket are not a digit/letter or a \*
        if (not eqn[pos - 1].isdigit()) or (not eqn[pos - 1].isalpha()) or (eqn[pos - 1] not in "/*"):
            OBpositions.remove(pos)
    
    # tempList = bracketPositions.copy() # the positions of all the brackets in the string

    #(2x+4)-3x+4x^2-3(12x-3)+4/(3+2x)
    # for pos in tempList:
        # if (pos == 0) or (pos == len(eqn) - 1):
        #     continue
        # else: 
        #     if eqn[pos + 1] in "+-" or eqn[pos - 1] in "+-":
        #         bracketPositions.remove(pos)

    for idx, bpos in enumerate(bracketPositions):
        if idx % 2 == 0 and idx + 1 < len(bracketPositions):
            print(f"{bpos} : {idx} && {bracketPositions[idx + 1]} : {idx + 1}")
            print("--------------------------->" + eqn[bpos:bracketPositions[idx + 1] + 1])

        elif idx % 2 == 0:
            print("--------------------------->" + eqn[bpos + 1:])

        
    # else:
    #     for pos in range(1, len(tempList) - 1):
    #         if (eqn[tempList[pos] + 1] in "*/^") or (eqn[tempList[pos] - 1] in "*/^"):
    #             bracketPositions.remove(tempList[pos])

    # print(eqn[bracketPositions[0]:bracketPositions[1] + 1])
    
    print(bracketPositions)

    return eqn.split() # fix this 

def eqnParserHelper(bracketPos: list[int], eqn: str, openBracket: bool) -> list[int]:
    temp = bracketPos.copy()
    # if the characters beside each bracket match the condition, else remove the bracket position
    for pos in temp:
        condition = eqn[pos - 1] not in "0123456789abcdefghijklmnopqrstuvwxyz/*^" and (
            eqn[pos + 1] not in "0123456789abcdefghijklmnopqrstuvwxyz/*^")

        if condition:
            bracketPos.remove(pos)
    
    return bracketPos


print("\n")
print(equationHandler(")/(") + "\n")
print(equationHandler("4x + (3x^2)^2 + 1") + "\n")
# print(equationHandler("(6x^3)/-9x+4") + "\n")
# print(equationHandler("(2x+4)-3x+4x^2-3(12x-3)+4/(3+2x)") + "\n")
# print(equationHandler("(2x+4)+(12x-3)+(4x^2)/(3+2x)") + "\n")