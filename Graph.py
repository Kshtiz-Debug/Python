"""
import matplotlib.pyplot as plt
import numpy as np

# Generate x values (angles)
x = np.linspace(0, 2 * np.pi, 100)  # Create 100 points from 0 to 2*pi

# Calculate corresponding y values (sine of x)
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("Angle (radians)")
plt.ylabel("sin(angle)")
plt.title("Sine Wave")

# Add a grid
plt.grid(True)

# Display the plot
plt.show()

"""

import math

x=3.14159265359
z=(math.sin(x/2))
y=int(math.ceil(z))
print(z,"----",y)
