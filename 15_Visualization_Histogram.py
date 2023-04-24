#
# Template for python program
# Name:
#

import matplotlib.pyplot as plt
import numpy as np 

# 1. Input
xpoints= np.random.normal(170,10,100)


# 2. Process

# 3. Output
plt.title("Histogram: Michael")
plt.grid()
plt.hist(xpoints)
plt.show()