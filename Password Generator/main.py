import random

print("Here is your Passowrd Generator")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,?'

number = input("enter password quantity: ")

number = int(number)

length = input("enter length of your password: ")

length = int(length)

print('\nHere are your passwords generated-')

for password in range(number):
    pwd = ''
    for i in range(length):
        pwd += random.choice(characters)
    print(pwd)