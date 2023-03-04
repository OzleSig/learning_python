text_w="Hi\nThis is a test\nI am writing a file"
text_a="\nNew text alert! I have appended.\nSee Ya!"

with open('test.txt','w') as file: # w argument in open function writes/overwrites text
    file.write(text_w)

with open('test.txt','a') as file: # a argument in open function appends text
    file.write(text_a)

with open('test.txt','r') as file: #opens file for reading
    for line in file:              #reads lines in file
        print(line)                #prints lines