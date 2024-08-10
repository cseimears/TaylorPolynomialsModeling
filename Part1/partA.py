import numpy as np
import matplotlib.pyplot as plt

def y(x):
    return np.exp(x*np.sqrt(1-x))

def taylor_series(x, n):
    series = 0
    for i in range(n+1):
        y_deriv = y_i = y(x)
        for j in range(i):
            y_deriv = (y_deriv*(j+1-x)+y_i*x)/(j+1)
        series += y_deriv*(x**i)/np.math.factorial(i)
    return series

# Define the range of x values
x = np.linspace(0, 3.5, 1000)

# Calculate the actual solution and the Taylor series up to n=4
y_actual = y(x)
y_taylor = taylor_series(x, 4)

# Plot the actual solution and the Taylor series
plt.plot(x, y_actual, label='Actual')
plt.plot(x, y_taylor, label='Taylor')
plt.legend()
plt.show()
