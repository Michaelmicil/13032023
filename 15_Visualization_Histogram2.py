#
# Template for python program
# Name:
#

import matplotlib.pyplot as plt
import numpy as np 

# 1. Input
xpoints= np.random.normal(90,10,100)


# 2. Process

# 3. Output
plt.title("Histogram: Michael")
plt.xlabel("Distribution")
plt.ylabel("Score")

plt.xlim([0,100])
plt.hist(xpoints)
plt.show()