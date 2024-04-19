#This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with x's)
#It will then accept a second number of any length and display the last 4 digits.
#Author: Paul Cahill
   
account_no = str(input("Please input your 10 digit account number: "))
if len(account_no) > 10:     print("The number you entered has too many characters. Next time enter a 10 digit account number")
if len(account_no) < 10:     print("The number you entered has too few characters. Next time enter a 10 digit account number")
if len(account_no) == 10:    print (f"Your account number is XXXXXX{account_no [5:9]}")

#if account numbers of any length are accepted my assumptions are that:
#everyone has two accounts, one with 10 digits and a second with any number of digits
#for the second account, if 4 or less digits are entered they will all be displayed.
#this program accepts letters as well as numbers (as does the 10 digit one).

second_no = str(input("What is your second account number (this can be of any length)?: "))
second_no_X = 'X' * (len(second_no) - 4)
second_no_last_4_digits = second_no[-4:]
print (f"Your second account number is: {second_no_X}{second_no_last_4_digits}")

#References:
#W3 Schools Guide to Python types: https://www.w3schools.com/python/python_datatypes.asp
#W3 Schools Guide to If Statements: https://www.w3schools.com/python/python_conditions.asp
#Stack Overflow thread on similar issue: https://stackoverflow.com/questions/40842451/how-do-i-use-the-replace-function-to-change-all-but-the-last-4-characters-of