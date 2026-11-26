"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    
    if b_text == 0 and operation == "/":
        status = "ERROR"
        result = ""
        error_code = "DIVISION_BY_ZERO"
    
    elif operation != "+" and operation != "-" and operation != "*" and operation != "/":
        status = "ERROR"
        result = ""
        error_code = "UNKNOWN_OPERATION"
    
    elif type(a_text) != float or type(b_text) != float:
        status = "ERROR"
        result = ""
        error_code = "INVALID_NUMBER"
    
    else:
        status = "OK"
        error_code = ""
    
        if operation == "+":
            result = add(a_text, b_text)
    
        elif operation == "-":
            result = subtract(a_text, b_text)
    
        elif operation == "*":
            result = multiply(a_text, b_text)
    
        elif operation == "/":
            result = divide(a_text, b_text)
    
    return(status, result, error_code)
    
    
    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """
