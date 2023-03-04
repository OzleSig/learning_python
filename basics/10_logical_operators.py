#logical operator (and/or/not) = used to check if two or more conditional statements are true

temp = int(input("what is the temp outside?: "))

#if (temp >= 0 and temp <= 20): #both conditions must be true for next part to happen
   # print ("Not summer yet")
   # print ("Stay indoors.")
#elif (temp < 0 or temp > 20): #if one is true, entire statement is true
 #   print ("The temprature is extreme today!")
  #  print ("don't go outside.")

#not reverses the true/false of conditional statement i.e. if it's NOT xyz then it's true

if not(temp >= 0 and temp <= 20): 
    print ("Not summer yet")
    print ("Stay indoors.")
elif not(temp < 0 or temp > 20):
    print ("The temprature is extreme today!")
    print ("don't go outside.")
