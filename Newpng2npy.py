import numpy as np
from PIL import Image
i = 0
nnpy = []
for a in range(10000):
    data = 'D:/ieeedata/X_train/X%d.png' % (a)
    with Image.open(data) as f:
        npy = np.array(f)
    #npy = npy.tolist()  # array转list不一定对需要验证
    nnpy.append(npy)  # 把npy加起来（把单张图片加起来）
    print(i)
    i = i + 1
np.save('train.npy', nnpy)