import matplotlib.pyplot as plt
from datetime import datetime
from scipy.ndimage.filters import gaussian_filter1d, gaussian_filter
from scipy import interpolate
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

f = open('data/nvwater.txt','r')
lines = f.readlines()

#print("----------------------------------------------------------")

codesRaw=lines[12786:12958]
codesDict={"fields":{}}

format=lines[12959][:-2].split("\t")
huh=lines[12960][:-2].split("\t")
data=lines[12961:278769]

#print(format)
#print(data[0][:-2].split("\t"))

#print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

key1 = "fields"

for el in codesRaw:
    status=el[2:-2].split()
    if len(status)==0:
        continue
    elif status[0]=="Referenced":
        for elf in status[1:]:
            if elf[0]=="(":
                key1=elf[1:-1]##search for key in ()
                codesDict[key1]={}
        #print(key1)
    else:
        key2=status[0]
        phrase=""
        for a in status[1:]:
            phrase=phrase+" "+a
        codesDict[key1][key2]=phrase[1:]

#print(codesDict["lev_acy_cd"])

#print("###########################################")

f2 = open('data/gwsites.txt','r')
lines2 = f2.readlines()

names=lines2[12:24]
titles=lines2[32]
sitesRaw=lines2[34:]



#rint(titles)

siteDict={}

for name in names:
    key=name.split()[1]
    phrase=""
    for a in name.split()[3:]:
        phrase=phrase+" "+a
    siteDict[key]=phrase[1:]

sites={}

for site in sitesRaw:
    sp=site.split("\t")
    id=sp[0]
    sites[id]={"data":{}}
    for i in range(12):
        key=titles.split()[i+1]
        if key!="coord_acy_cd'" and key!="dec_coord_datum_cd" and key!="alt_datum_cd" and key!="alt_acy_va":
            if key=="gw_count_nu":
                sites[id][key]=sp[i+1][:-1]
            else:
                sites[id][key]=sp[i+1]
    if int(sites[id]["gw_count_nu"])>2000:
        print(id)
        


#print(sites['331923114513301'])

dates=[]
count=[]
idn='360349115100001'
for pt in data:
    dat=pt[:-2].split("\t")
    if dat[1]==idn:
        dates.append(datetime.fromisoformat(dat[3]).timestamp()/31536000+1970)
        count.append(-1*float(dat[6]))
y = gaussian_filter1d(count, sigma=2)
#plt.plot(dates,y)
#plt.show()

def isNumber(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        return False
    return True


x2=[]
y2=[]

for site in sitesRaw:
    sp=site.split("\t")
    id=sp[0]
    
    lon=sites[id]["dec_lat_va"]
    lat=sites[id]["dec_long_va"]
    
    if isNumber(lon) and isNumber(lat) and int(sites[id]["gw_count_nu"]):
        lon=float(lon)
        lat=float(lat)
        
        x2.append(lat)
        y2.append(lon)
    
#plt.scatter(y2,x2)#,alpha=0.1)
#plt.show()

#985,722,613
timeData=np.zeros((90,722,613))
ref=np.zeros((90,722,613))

for pt in data:
    dat=pt[:-2].split("\t")
    id=dat[1]
    
    #print(dat[1]==idn)
    if isNumber(dat[6]):
        val=float(dat[6])
        if len(dat[3])==7:
            dat[3]+="-01"
        if len(dat[3])==4:
            dat[3]+="-01-01"
        sites[id]["data"][dat[3]]=val
        #month=(int(dat[3][:4])-1938)*12+int(dat[3][5:7])
        year=int(dat[3][:4])-1938
        lon=sites[id]["dec_lat_va"]
        lat=sites[id]["dec_long_va"]
        if isNumber(lon) and isNumber(lat) and int(sites[id]["gw_count_nu"]):
            lon=(float(lon)-34.8)*100
            lat=(float(lat)+120.17)*100
            num=ref[year,int(lon),int(lat)]
            timeData[year,int(lon),int(lat)]=(num*timeData[year,int(lon),int(lat)]+val)/(num+1)
            ref[year,int(lon),int(lat)]+=1

fig = plt.figure()
ax = plt.axes()  

plt.title('Water Visualization')

#z = timeData[50,:,:]
#z = np.flip(np.flip(gaussian_filter(timeData[500,:,:],sigma=6)),1)
#cont = plt.imshow(z)

co=0
for i in range(timeData.shape[1]):
    for j in range(timeData.shape[2]):
        con=0
        for k in range(timeData.shape[0]):
            if timeData[k,i,j]!=0:
                con+=1
        if con>3:
            co+=1
    print(i,end='\r')
print(co)

##baseline
#for i in range(timeData.size)



plt.show()

# Animation function
#def animate(i): 
#    z = gaussian_filter(timeData[i,:,:],sigma=3)
#    #z = data[:,:,i]
#    cont = plt.imshow(z)
#    
#    print(i,end='\r')
#    return cont  

#anim = FuncAnimation(fig, animate, frames=timeData.shape[0])
#anim.save('basic_animation.gif', writer=PillowWriter(fps=24))

#plt.show()



#np.save('timeData',timeData)

#a=[]
#dataPts=np.array([2,3,4])
#for k in range(938):
#    count=0    
#    for i in range(720):
#        for j in range(613):
#            if 0!=timeData[k,i,j]:
#                count+=1
            #np.append(dataPts,[k/12+1938,timeData[k,i,j]])
#    a.append(count)
#    if k%10==0:
#        print(k/10, end='\r')
#plt.plot(gaussian_filter1d(a, sigma=3))
#plt.show()   
    



#for site in sitesRaw:
#    sp=site.split("\t")
#    idn=sp[0]
#    arr=np.array([])
#    if int(sites[idn]["gw_count_nu"])>200:      
      
       # np.append(arr,[datetime.fromisoformat(dat[3]).timestamp()/31536000+1970,float(dat[6])])
                
        #y = gaussian_filter1d(lev, sigma=2)
        #plt.plot(dates,y)
        #plt.show()


#print(sites['393309118515901'])     


def isNumber(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False

    return True