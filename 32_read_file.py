
try:
    with open('//Users//ozlemsigbeku//Documents//Data//Python_Work//Test.tx') as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print ("that file was not found :(")