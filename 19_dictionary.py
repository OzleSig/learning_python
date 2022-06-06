capitals = {'USA':'Washington DC', 
            'India': 'New Dehli',
            'Turkey': 'Ankara',
            'UK': 'London'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('India')
#capitals.clear()

#print(capitals['UK'])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items ():
    print(key, value)