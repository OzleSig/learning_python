# nested function calls = functions inside other function calls
#                         innermost function calls are resolved first

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
# all the above is written in one line of code below

print(round(abs(float(input("Enter a whole positive number: ")))))