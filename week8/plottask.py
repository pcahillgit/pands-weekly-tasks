#In this final task I will write a program that displays
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
#and a plot of the function h(x)=x3 in the range 0 to 10, 
#on the one set of axes.
#Author: Paul cahill

#Libraries (numpy is used for creating multidimensianal arrays and matplotlib is used for plotting)
import numpy as np
import matplotlib.pyplot as plt

#histogram
#defining the mean, standard deviation and number of values
mean = 5
std_dev = 2
num_values = 1000
#generating 1000 random values in Guassian distribution
data = np.random.normal(mean, std_dev, num_values)

#plotting the histogram (the 1000 values, how many bins in the histogram, colour, label for the legend, surrounding bins in black outline)
plt.hist(data, bins=20, color='blue', label='Normal Distribution', edgecolor='black')

#function
#x is a number between 0 to 10, this is done 100 times
x_values = np.linspace(0, 10, 100)
#y is x to the power of 3
y_values = x_values ** 3
#plotting, the $'s are used for LaTex mathematical notation
plt.plot(x_values, y_values, color='red', label='$h(x) = x^3$')

#setting the axis labels, title, legend and grid
plt.xlabel('Distribution Values / x')
plt.ylabel('Frequency of Distribution Values / h(x)')
plt.title('Histogram of Normal Distribution and Plot of $h(x) = x^3$')
plt.legend()
plt.grid(True)

#display
plt.show()

#References:
#W3 Schools Guide to Matplotlib: https://www.w3schools.com/python/matplotlib_intro.asp
#RealPython Matplotlib Guide: https://realpython.com/python-matplotlib-guide/
#Numpy for beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
#LaTex mathematical notation, using the $ symbols to add mathematical notation style: https://patrickwalls.github.io/mathematicalpython/jupyter/latex/