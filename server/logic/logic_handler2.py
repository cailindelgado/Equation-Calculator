class ParseError(Exception):
    pass


def equationHandler(eqn: str) -> str:
    try:
        eqnBits = Parser(eqn)
        eqn = ""
        for bit in eqnBits:
            eqn += bit
    except ParseError as e:
        eqn = str(e)

    return eqn


def Parser(eqn: str) -> list[str]:
    eqn = eqn.strip().replace(" ", "")

    checkEqn(eqn)  # Check if valid

    OBpos = []
    CBpos = []

    for pos, char in enumerate(eqn):
        if char in "({[]})":
            if char in "({[":
                OBpos.append(pos)
            else:
                CBpos.append(pos)

    return eqn.split()


def checkEqn(eqn: str) -> None:

    stack = []
    brackets = {"}": "{", "]": "[", ")": "("}

    for char in eqn:
        # check if any weird chars
        if char in "~!@#$%7`_=\\|'\":;?<>,":
            raise ParseError(f"Invalid character: {char}")


        # check brackets

        if char in brackets:  # ({[
            stack.append(char)
        elif char in brackets.values():  # )}]
            if not stack or brackets[stack.pop()] != char: 
                raise ParseError(f"Invalid brackets used {char}")

        # check unusual stuff e.g ^) or (/ or x.y

    return
