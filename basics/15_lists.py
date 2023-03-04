# list = used to store multiple items in a single variable

food = ["pizza","cheesburger", "hotdog", "cheese"]

food[3] = "sarma"

print (food[3], food[2])

food.append("crackers")
food.remove ("hotdog")
food.pop()
food.insert(0,"wrap")


for x in food:
    print(x)

food.sort()

for x in food:
    print(x)

food.clear()