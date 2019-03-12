import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation, PillowWriter
#import cartopy

data=np.load('grace.npy')


#print(data.shape)

#print(data[0,0,:].shape)
a=360
b=180

new = np.zeros((a,b))

for i in range(a):
    for j in range(b):
        y = data[i,j,:]
        x = np.linspace(0.0, y.size, num=y.size)
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        #plt.plot(x, y, 'o', label='Original data', markersize=10)
        #plt.plot(x, m*x + c, 'r', label='Fitted line')
        #plt.legend()
        #plt.show()
        new[i,j]=m
plt.imshow(np.flip(np.rot90(new,axes=(1,0))),vmin=-0.1, vmax=0.1)

#plt.hist(new, bins=[-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6])  # arguments are passed to np.histogram
#plt.title("Histogram with 'auto' bins")
#plt.show()


#plt.figure(figsize=(6, 3))
#ax = plt.axes(projection=cartopy.crs.PlateCarree(central_longitude=180))
#ax.coastlines(resolution='110m')
#ax.gridlines()

plt.show()