import numpy as np
import matplotlib.pyplot as plt

def f(x, y, dy):
    return (x - 2)*dy - 2*y

def taylor_poly(x, y, dy, h):
    y1 = y + h*dy + (h**2/2)*f(x, y, dy)
    dy1 = dy + h*f(x, y, dy)
    y2 = y1 + h*dy1 + (h**2/2)*f(x+h, y1, dy1)
    return y2

# Initial conditions
x0 = 3
y0 = 1
dy0 = 2

# Step size
h = 0.1

# Number of steps
n = 30

# Initialize arrays to store x and y values
x = np.zeros(n+1)
y = np.zeros(n+1)

# Set initial values
x[0] = x0
y[0] = y0

# Calculate Taylor polynomial and store values in arrays
for i in range(n):
    y[i+1] = taylor_poly(x[i], y[i], dy0, h)
    x[i+1] = x[i] + h

# Plot the Taylor polynomial
plt.plot(x, y, label='Taylor polynomial')

# Calculate exact solution
xe = np.linspace(x0, x0 + n*h, 100)
ye = y0*np.exp(xe - x0) + (dy0/2)*(np.exp(xe-x0) - np.exp(-xe+x0))

# Plot exact solution
plt.plot(xe, ye, label='Exact solution')

# Set plot options
plt.title('Second-order Taylor polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show plot
plt.show()
