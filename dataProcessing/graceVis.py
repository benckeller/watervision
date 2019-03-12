import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

data=np.load('grace.npy')
print(data.shape)



#plt.imshow(np.flip(np.rot90(data[:,:,260],axes=(1,0))))
#plt.show()


# Set up plotting
fig = plt.figure()
ax = plt.axes()  

plt.title('GRACE Visualization 2002-2017')

# Animation function
def animate(i): 
    z = np.flip(np.rot90(data[:,:,i],axes=(1,0)))
    #z = data[:,:,i]
    cont = plt.imshow(z)
    
    print(i)
    return cont  

#anim = FuncAnimation(fig, animate, frames=data.shape[2])
#anim.save('basic_animation.gif', writer=PillowWriter(fps=24))

#plt.show()