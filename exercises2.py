def str_to_no(x):
    first_part = (x.split('.'))[0]
    power = len(first_part)-1
    number = 0
    for char in x:
        multiplier = pow(10, power)
        no = ord(char)
        if not ((no >= 48 and no <= 57) or (no == 46)):
            return ('not a number')
        elif not (no == 46):
            number = number + (no - 48)*multiplier
            power -= 1
    return number
    


#print(str_to_no('10.09'))


