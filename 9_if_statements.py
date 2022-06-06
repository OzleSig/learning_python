age = int(input("How old do you think I am?: "))

if age > 26 and age <=122:
    print("Too old! Don't be so rude.")
elif age == 26:
    print ("Well done. You are correct. Good for you.")
elif age < 0:
    print ("Do you think I haven't been born yet? Why would you even suggest that?")
elif age > 122:
    print("You think I'm older than the oldest person alive? Well, that's just silly.")
else:
    print("Too young. You are incorrect.")