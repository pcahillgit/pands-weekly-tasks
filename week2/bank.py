#This program will take two amounts in cents and combine them to give a total in euro.
#Author: Paul cahill

Number1 = int(input('Enter your first amount (in cents): '))
Number2 = int(input('Enter your second amount (in cents): '))
Total = (Number1 + Number2) / 100
print (f'The sum of these is €{Total}')

#References:
#W3 schools guide to Python types: https://www.w3schools.com/python/python_datatypes.asp