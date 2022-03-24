try:
    a = 10
    b = 0
    c = a / b
    print(c)

except ZeroDivisionError as e:  # e denotes the object name !!!
    print("Not Possible" + str(e))

except:
    print("Division By Zero Not Possible")


else:
    print("Executed Successfully")

finally:
    print("Harman Connected Services")