# Part A

This program calculates and plots the Taylor series for the 
function y(x) = e^(x*sqrt(1-x)) up to n=4, and compares it to 
the actual solution. The program defines two functions, y(x) and 
taylor_series(x,n), which respectively compute the value of y at 
a given x and the value of the Taylor series at a given x up to 
a given degree of n.

The main function then generates a range of x values, calculates 
the actual solution and the Taylor series at each of these x 
values, and plots both functions on a graph using Matplotlib.

# Part B

This program calculates and plots the second-order Taylor 
polynomial for the function y(x) = x^2 - 3x + 15 centered at 
x=3. The program defines two functions, y(x) and taylor_poly(x), 
which respectively compute the value of y at a given x and the 
value of the Taylor polynomial at a given x.

The main function then generates a range of x values, calculates 
the actual solution and the Taylor polynomial at each of these x 
values, and plots both functions on a graph using Matplotlib.

# Running the programs

Ensure that python, matplotlib, and numpy are installed.

use the following commands respectively to run the programs.

'python partA.py' 

'python partB.py'

# Analysis

In both programs, Matplotlib is used to plot the functions on a 
graph and the graph is displayed to the user using the 
plt.show() function.

The convergence of the Taylor series in partA and the accuracy 
of the Taylor polynomial in partB depend on the choice of 
function and the range of x values used. The user may modify the 
input values in the main function to observe the convergence and 
accuracy of the Taylor series or polynomial for different 
functions and input ranges. However, the inputs to the programs
are tailored to the assignment.
