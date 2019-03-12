from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

data=[[[1,0,9,11,0,6,0,14,0,18],[1,4,0,8,0,6,0,0,11,14]],[[4,5,0,3,0,7,8,0,12,14],[1,2,0,0,6,0,8,13,16,19]]]

def interp(a):
    #remove all zeroes
    x=np.linspace(0, a.size, num=a.size, endpoint=True)
    ind=[]
    for i in range(a.size):
        if a[i]==0:
            ind.append(i)
    a2 = np.delete(a,ind)
    x2 = np.delete(x,ind)  
    #print(a2,x2)  
    f = interp1d(x2, a2, kind='cubic')
    return f(x)

a= np.apply_along_axis(interp,2,data)
print(a)
#print(x)