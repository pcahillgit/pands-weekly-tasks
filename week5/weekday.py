#This program will tell the user if it is a weekday or weekend.
#Author: Paul Cahill

import time
#Pythons time module can be used to pull the systems current time.
date = time.asctime()
#Here, the date variable will contain the system time, with the day abbreviated (this will be the first three characters).
if date[:3] in ["Mon", "Tue", "Wed", "Thu", "Fri"]: 
    print ("It's a weekday, get back to work.")   
else:   
    print ("It's the weekend!!!")
#If the date string's first three characters contains any of the weekday substrings listed above then it is a weekday.
#Python indexing starts at 0 so we're looking for characters 0,1 & 2. That is [:3].
#If the substring is not present then it's the weekend, yay!