# **kwargs = parameters that will pack all arguments into dictionary 
#            useful so that function can accept varying amount of key word arguments

def hello (**kwargs):
#    print ("Hello " + first + " " +last)
    print ("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title= "Mrs", first="Ozlem", middle= "Cutie", last="Sigbeku")