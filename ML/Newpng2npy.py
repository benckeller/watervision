import numpy as np
from PIL import Image
i = 0
nnpy = []
for a in range(10000):
    data = './data/%d.%s' #File name and type
    with Image.open(data) as f:
        npy = np.array(f)
    #npy = npy.tolist()  # Need verification to turn array into list
    nnpy.append(npy)  # add up npy (append each single image)
    print(i)
    i = i + 1
np.save('train.npy', nnpy)