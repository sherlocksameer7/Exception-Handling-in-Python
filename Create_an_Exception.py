try:
    age = 17
    if age > 18:
        raise ValueError("Voting Age is Minimum 18+")
    else:
        print("Eligible for Voting !!! ")


except ZeroDivisionError as e:  # e denotes the object name !!!
    print("Division By Zero Not Possible" + str(e))


except ValueError as e:
    print("User-defined Exception" + str(e))


except:
    print("Exception Occured")


else:
    print("Executed Successfully")



finally:
    print("Harman Connected Services")