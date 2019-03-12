import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

data=np.load('grace.npy')
print(data.shape)


#plt.imshow(dataset[100])
#plt.show()




# Set up plotting
fig = plt.figure()
ax = plt.axes()  

# Animation function
def animate(i): 
    z = data[:,:,i]
    cont = plt.imshow(z)
    print(i)
    return cont  

anim = FuncAnimation(fig, animate, frames=data.shape[2])
anim.save('basic_animation.gif', writer=PillowWriter(fps=24))
plt.show()