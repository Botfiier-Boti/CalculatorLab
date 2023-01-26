def simple_calculate(operation, num1, num2):
    """
    Performs the given simple operation on the given numbers, which may be either integers or floats.

    args:
        - operation: the operation to perform (+, -, *, or /)
        - num1: the first number
        - num2: the second number

    returns:
        - the result of the operation on the given numbers
    """

    if operation == '+':
        return num1 + num2

    elif operation == '-':
        return num1 - num2

    elif operation == '*':
        return num1 * num2

    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError(
            'Invalid Operation: Simple Operations are (+, -, *, and /)')
