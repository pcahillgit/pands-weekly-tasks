#This program takes in a file as an argument on the command line and tells you how many times the letter e is in that file.
#I'm assuming that all e's, capitalised or not, accented or not, need to be counted from start to finish of the doc.
#Author: Paul Cahill

#importing sys which will allow us to access sys.argv (command line arguments)
import sys

#importing unicodedata which will allow us to turn accented e's into normal ones.
import unicodedata

#opening the file in read mode, converting accented e's into normal ones, counting the e's and printing result.
try:
    access_file = sys.argv[1]
#Accounting for non-text file:
    if not access_file.endswith('.txt'):
        print("File must be a .txt file, please try again.")
    else:
        with open(access_file, 'r') as file:
            content = file.read()
            #here, NFD is changing accented e's to normal ones
            normalise_content = unicodedata.normalize('NFD', content)
             # .lower converts the string to lower case
            e_count = normalise_content.lower().count('e')
            print(f"There are {e_count} e's in {access_file}.")

#Accounting for no argument:
except IndexError:
    print ("No argument provided, please provide a file (example: es.py test.txt)")

#Accounting for filename that doesnt exist:
except FileNotFoundError:
    print (f"File {access_file} not found, please try again.")

#References:
#Python Tutorials Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html
#W3 Schools Guide to If Statements: https://www.w3schools.com/python/python_conditions.asp
#Learning about command line arguments: https://www.geeksforgeeks.org/command-line-arguments-in-python/
#Similar stackoverflow thread: https://stackoverflow.com/questions/48885930/counting-specific-characters-in-a-file-python