from asyncore import read, write
from re import I

origin_doc = "/Users/ozlemsigbeku/Documents/programming/Data/Python_Work/Joy_coursework/measles.txt"
new_doc = input("Where would you like to put the pulled data: ")
syear = input("What year would you like to filter by: ")

def year_filt():
    with open(origin_doc) as original:
        og_file = original.readlines()

    with open(new_doc, 'w') as new_file:
        for line in og_file:
            year = line[88:92]
            if  year.startswith(syear) or syear.lower() == "all":
                new_file.write(line)

    with open(new_doc) as file:
        file = file.readlines()
        print(file)
year_filt()