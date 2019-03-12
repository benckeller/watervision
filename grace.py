import numpy as np
import os

directory = os.fsencode('data/GRACE/10day/water/')

dataset=np.zeros((360,180,454))

count=0
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".txt"): 
        #print(filename)
        
        print(count)
        f = open("data/GRACE/10day/water/"+filename, "r")
        date=f.read(335)[317:334]
        data = np.loadtxt("data/GRACE/10day/water/"+filename, skiprows=12)
        
        
        for i in range(int(data.size/3)):
            #print(data.size)
            dataset[int(data[i][0]-0.5)][int(data[i][1]+89.5)][count]=data[i][2]
        count+=1
        continue
     else:
        continue
print(dataset[0:3])
np.save('grace',dataset)