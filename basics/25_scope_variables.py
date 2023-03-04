#scope = a region that a variable is recognised

name = "Ozlem"# global scope (available inside and outside functions)

def display_name():
    #name = "Sigbeku" # local scope (available only inside this function)
    print(name)

display_name()
print(name) #will not work

#Python wil use LEGB principle (1. Local, 2. Enclosing, 3. Global, 4. Built in)