# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept varying amount of arguments

def add (*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))

def add (*stuff): #works the same as args, make sure "*" before
    sum = 0
    stuff = list(stuff) #need to cast it to a list before changing one of the values (as linebelow)
    stuff[0] = 0 # changing value at index 0 "[0]" won't work without above because tuples are unchangable
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))