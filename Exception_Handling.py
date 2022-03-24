# Types of Exceptions in Python are ZerDivisionError, NameError, IOError, ValueError, EOFError

try:
    a = 10
    b = 0
    c = a / b
    print(c)

except ZeroDivisionError:
    print("Not Possible")                # Multiple Exceptions are Applicable...

except:
    print("Division By Zero Not Possible")