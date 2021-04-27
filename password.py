import random

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP123456789#!@"
while 1:
    password_len = int(input('how many characters would you like your password to have: '))

    password_count = int(input('how many passwords would you like : '))
    #a for loop for number of passwords and assigning an empty string to it

    for x in range(0, password_count):
        password = " "
    #a for loop for picking random characters from  var chars
        for x in range(0, password_len):
           password_char = random.choice(chars)
           password = password + password_char
           print('here is your new password:',password)