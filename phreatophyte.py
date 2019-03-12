from scipy import ndimage
import imageio
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray

img = imageio.imread('phreatophytes.tif')

image=rgb2gray(img)
g = np.zeros((image.shape[0],image.shape[1],3))
#print(type(image))  
print(image.shape)
#print(image.dtype)
mask =(image < .46)
g[mask] =[1,1,1]
g=ndimage.rotate(g,14)
#print(rota[4000][1200:1400])
#print(rota.shape)
#print(mask[4000][1200:1400])
plt.imshow(g, cmap='gray')
plt.show()
#plt.imshow(rota, cmap='gray')
#plt.show()
