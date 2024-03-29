# What is Matplotlib?
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.
# Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.
import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0, 6])
ypoint = np.array([0, 250])
plt.plot(xpoint, ypoint)
plt.show()

xpoint = np.array([0, 2, 5, 6])
ypoint = np.array([0, 4, 6, 12])
plt.plot(xpoint, ypoint, 'o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o', linestyle = 'dotted', ms=15, mec='r', mfc='g')
plt.show()