def calc():
    print("Calculator: ")
    expr = input(" Enter the equation you want to solve: \n")
    try:
        result = eval(expr)
        print("Calculating.....")
        print("Result: ", result)
    except {ValueError, SyntaxError, ZeroDivisionError, NameError} as e:
        print("Error: Invalid Expression")
calc()
