#
# Template for python program
# Name:
#

import matplotlib.pyplot as plt
import numpy as np 

# 1. Input
xpoints= np.random.normal(170,1,100)


# 2. Process

# 3. Output
plt.title("Histogram: Michael")
plt.xlabel("Distribution")
plt.ylabel("Score")

plt.xlim([140,200])
plt.hist(xpoints)
plt.show()