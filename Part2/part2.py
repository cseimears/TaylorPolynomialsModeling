import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(y, x):
    dydx = [y[1], (x**2 + 4)*y[1] + y[0] - x]
    return dydx

# initial conditions
y0 = [0, 0]

# x values to solve for
x = np.linspace(0, 1, 101)

# solve the differential equation
sol = odeint(f, y0, x)

# plot the solution
plt.plot(x, sol[:, 0], label='y')
plt.plot(x, sol[:, 1], label="y'")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
