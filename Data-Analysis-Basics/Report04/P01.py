import numpy as np
import matplotlib.pyplot as plt

ndarray = np.random.randint(50, size=(2, 30))

plt.scatter(ndarray[0], ndarray[1])
plt.show()
