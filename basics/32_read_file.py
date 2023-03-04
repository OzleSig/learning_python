
try:
    with open('//Users//ozlemsigbeku//Documents//Data//Python_Work//Test.txt') as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print ("that file was not found :(")