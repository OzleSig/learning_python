from ast import Not
from cmath import e
from re import X
import sys

def get_user_file():
    while 1:
        og_doc = input("What document would you like to open?: ")
        try:
            with open(og_doc) as og_file:
                return og_file.readlines()
        except Exception as e:
            print(repr(e) + " Input full file name with extension (i.e. .docx .txt)")
           
data = get_user_file()
#print(data)

print("Please enter income to filter by")
print("1 - lower income") 
print("2 - lower middle income") 
print("3 - middle income") 
print("4 - high income")
income_filt = int(input(": "))
year_filt = input("Please enter a year to filter by:")
if income_filt == 1:
    income_filt = "WB_LI "
elif income_filt == 2:
    income_filt = "WB_LMI"
elif income_filt == 3:
    income_filt = "WB_UMI"
elif income_filt == 4: 
    income_filt = "WB_HI "

output = 1
for line in data:
    year = line[88:92]
    income = line[51:57]
    if  year.startswith(year_filt) or year_filt.lower() == "all" and income_filt == income:
        output = line
#   print(income)
#    print(output)    

