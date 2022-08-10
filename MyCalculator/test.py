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
    sm_test.stringmath_string()
    sm_test.append_string("+")
    sm_test.stringmath_string()
    sm_test.append_string("5")
    sm_test.append_string("+")
    sm_test.stringmath_string()

run_test()