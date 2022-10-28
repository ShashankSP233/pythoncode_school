import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,50,14)
x1=np.arange(1,30,14)
y=np.log(x)
y1=np.cos(x1)
plt.scatter(x,y)

plt.show()