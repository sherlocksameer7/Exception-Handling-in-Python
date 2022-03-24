try:
    a = 10
    b = 5
    c = a / b
    print(c)

except ZeroDivisionError:
    print("Not Possible")                # Multiple Exceptions are Applicable...

except:
    print("Division By Zero Not Possible")


else:
    print("Executed Successfully")