#Unit Testing for MyCalculator

from mycalc import *

def run_test():
    StringMath_test()

def StringMath_test():
    sm_test = StringMath()
    if StringMath.validate_operator("5"):
        print("VALID OPERATOR")
    else:
        print("INVALID OPERATOR")
    sm_test.string()
    sm_test.append("+")
    sm_test.string()
    sm_test.append("5")
    sm_test.append("+")
    sm_test.string()

    sm_test2 = StringMath()
    sm_test2.append("5 + 2 * 3 / 4")
    sm_test2.string()
    print(sm_test2.execute_string())

    sm_test3 = StringMath("5 + 2")
    sm_test3.string()

run_test()