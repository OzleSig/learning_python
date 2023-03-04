#tuple = collection which is ordered and unchangable used to group together related data

student = ("Oz", 26, "female")

print(student.count("Oz"))
print(student.index("female"))

for x in student:
    print (x)

if "Oz" in student:
    print ("Oz is here!")