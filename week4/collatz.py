#This program will prompt the user to enter a positive integer and then prints the successive values of the following calculation:
#at each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#The program will stop once it reaches 1.
#Author: Paul Cahill

while True:
    try:    
        number = int(input("please enter a positive integer: "))
        if number <= 0: 
           raise ValueError    
        break   
    except ValueError:
        print("The number you have entered must be a positive integer, please try again.")
#Above, we are prompting the user to enter a number. If the number is not a positive integer (less than 0) it will not be accepted.


while number > 1:  
    print (number, end=' ')
    if (number % 2) == 0:   
        number = number // 2  
    else: 
        number = (number * 3) + 1
else:   
    print (number, end=' ')
#Above, we are specifying the calculations to take place if the number is above 1. Each step in the calculation will print in sequence, always ending in 1.

#References:
#W3 Schools Guide to If Statements: https://www.w3schools.com/python/python_conditions.asp
#Python Guides Flows: https://docs.python.org/3/tutorial/controlflow.html