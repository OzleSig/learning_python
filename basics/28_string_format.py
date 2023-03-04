#str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumoed over the "+item)
#print("The {} jumped over the {}".format(item,animal))
#print("The {1} jumped over the {0}".format(item,animal)) #positional argument
#print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "Oz"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}".format(name))
#print("Hello, my name is {:<10}".format(name))
#print("Hello, my name is {:>10}".format(name))
#print("Hello, my name is {:^10}".format(name))

#print("Hello, my name is {name:10}".format(name = "Popo"))
#print("Hello, my name is {0:<10}".format(name))

number = 100000000

print("The Number pi is {:.2f}".format(number))
print("The Number pi is {:,}".format(number))
print("The Number pi is {:b}".format(number))
print("The Number pi is {:o}".format(number))
print("The Number pi is {:X}".format(number))
print("The Number pi is {:E}".format(number))