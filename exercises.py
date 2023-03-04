# """ def one_to_100():
#     for x in range(100):
#         print(x+1)
# #one_to_100()

# def one_to_1000():
#     for x in range(1000):
#         print(x+1)
# #one_to_1000()

# def one_to_N(x):
#     for y in range(x):
#         print(y+1)
# #one_to_N(6)

# mixaroo = ['Star', 6, 'dew', 11]
# strings = ['Star', 'dew', 'valley']
# numbers = [1,23,76,92,1002,6,2,99,100]

# def list_fun(x):
#     for y in x:
#         print(y)
# #list_fun(numbers)

# def list_fun2(x):
#     for y in x:
#         print(y, end=' ')
# #list_fun2(numbers)
# #list_fun(strings)
# #list_fun(mixaroo)

# def list_increments(x):
#     for y in x:
#         print(y+1)
# #list_increments(numbers)

# def sum_list(x):
#     y = 0
#     for z in x:
#         y+=z
#     print(y)
# #a = sum_list(numbers)
# #print(a)
# #b = 10
# #a+=b
# #print(b)

# def sum_list2(x):
#     y = 0
#     for z in x:
#         y+=z
#     return y
# yo = sum_list2(numbers)
# print(yo)
# ay = 10
# ay+=yo
# print(ay) """

# numbers = [1,23,76,92,1002,6,2,99,100]

# def list_avg(x):
#     sum_list=0
#     number_list=0
#     for z in x:
#         sum_list+=int(z)
#         number_list+=1
#     avg_list = sum_list/number_list
#     return avg_list
# #avg = list_avg(numbers)
# #print(avg)

# def verify_input(number_list):
#     for number in number_list:
#         for charcater in number:
#             ascii_no = ord(charcater)
#             if not (48<=ascii_no and ascii_no<=57):
#                 return False
#     return number_list

# #ascii_check = 'blaj'
# #for x in ascii_check:
# #    ord(x) == 48-57

# def is_number(string):
#     for character in string:
#         if not (48<=ord(character) and ord(character)<=57):
#             return False
#     return True
# #check_is_no = is_number('1922')
# #print(check_is_no)

# def main():
#     input_list = input("Input a list of numbers delimited by a comma: ")
#     number_list = input_list.split(',')
#     if verify_input(number_list):
#         averages = list_avg(number_list)
#         print(averages)
#     else:
#         print('bitch no')

        
# main()

A = [5,4,2,3,1]
B = [7,9,10,67,9,2,78,3]


def bubble_sort(a_list):
    i = 0
    n = len(a_list)-1
    while i < n:
        for each_no in range(n):
            val1 = a_list[each_no]
            val2 = a_list[each_no+1]
            if val1>val2:
                a_list[each_no]=val2
                a_list[each_no+1]=val1
        print(a_list)
        i+=1

import random
randomlist = []
for i in range(0,50):
    n = random.randint(1,100)
    randomlist.append(n)

#bubble_sort(randomlist)

def is_even(x):
    return x % 2 == 0

def buzz_fizz():
    x = 1
    while x < 101:
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else: 
            print(x)
        x += 1
#buzz_fizz()

ascii_A = 65
ascii_N = 78
ascii_Z = 90
ascii_a = 97
ascii_n = 110
ascii_z = 122

def check_case(x):
    if ((x >= ascii_A) and (x <= ascii_Z)):
        return 'upper'
    elif ((x >= ascii_a) and (x <= ascii_z)):
        return 'lower'
    
def less_than_n(x):
    if (check_case(x) == 'upper') or (check_case(x) == 'lower'):
        return (check_case(x) == 'upper' and x < ascii_N) or ((check_case(x)) == 'lower' and (x < ascii_n))


def is_alphabet(x):
    x = ord(x)
    return ((x >= ascii_A) and (x <= ascii_Z)) or ((x >= ascii_a) and (x <= ascii_z))

def rot1320(secrets):
    encryption = ""
    for x in secrets:
        char = ord(x)
        lowercase = ord(x.lower())
        if is_alphabet(x):
            if (lowercase < ascii_n):
                encryption+=(chr(char+13))
            else:
                encryption+=(chr(char-13))
        else:
            encryption+=(chr(char))
    return encryption
                
            
def rot13(secrets):
    encrypt = ''
    for x in secrets:
        char = ord(x)
        if less_than_n(char) == True:
            char += 13
        elif less_than_n(char) == False:
            char -= 12
        x = chr(char)
        encrypt+=x
    return(encrypt)

#65-90 A-Z 97-122 a-z -13

def cypher13(secrets):
    decrypt = ''
    for x in secrets:
        char = ord(x)
        if less_than_n(char) == True:
            char += 12
        elif less_than_n(char) == False:
            char -= 13
        x = chr(char)
        decrypt+=x
    return(decrypt)

ooo = 'Joseph is a cute ass maNsS'
Oh = rot1320(ooo)
print(Oh)
#damn = cypher13(Oh)
#print(damn)