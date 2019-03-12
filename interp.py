import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

data=np.load('grace.npy')


#print(data.shape)

#print(data[0,0,:].shape)
a=67
b=54

y = data[a,b,:]
x = np.linspace(0.0, y.size, num=y.size)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()
