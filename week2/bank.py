# This program will take two amounts in cents and combine them to give a total in euro.

Number1 = int(input('Enter your first amount (in cents): '))
Number2 = int(input('Enter your second amount (in cents): '))
Total = (Number1 + Number2) / 100
print (f'The sum of these is €{Total}')