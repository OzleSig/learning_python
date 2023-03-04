#exception = events detected during execution that interrupts flow of program

from logging import exception


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print (e)
    print("You can't divide by zero! Idiot!")
except ValueError as e:
    print (e)
    print("Why would you divide that? Are you silly?")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")