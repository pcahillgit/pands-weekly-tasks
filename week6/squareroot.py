#This is a function that finds the approximated square-root of a given number.
#Author: Paul Cahill

def sqrt(inp):
    aprox = inp / 2
    for _ in range(50):
        aprox = (aprox + inp / aprox) / 2
    return round(aprox, 1)
#Here I am defining what my function will do to the given number.
#I am using Newtons-method for finding an approximated square number to guide my code.
#Newton's method involves a series of equations that provide results gradually converging towards the square-root of the given number.
#'_' can be used to repeat the equation multiple times and enter the aprox variable.
#The initial guess here is half of the given number.
#I went with 50 iterations of the equation as that seems to fairly accurately predict
#the square root for the numbers someone is likely to enter.
#Rounding to 1 decimal place as per the example given in the weekly task example on the VLE.

inp = float(input("please enter a positive number: "))
if inp < 0:
    print("That number is not positive, please try again")
#asking the user to enter a positive number. Using float here as decimals can be accepted.
else:   
    answer = sqrt(inp)
    print(f"The approximated square root of {inp} is {answer}")
#Once a valid input is given, the approximated squareroot of that number will be the output of the my function.
#It's a function so it's done in the background, the output is then printed as the answer.