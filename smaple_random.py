import math,random

f=open('data_binning.csv','r')
data=f.readlines()
length = 0.3*len(data)
f=open('sample_random','w')
number=[]
i=0
for _ in range(len(data)):

    if i > length:
        break
    num=random.randint(0,len(data))
    if num not in number:
        f.write(data[num])
        number.append(num)
        i=i+1
f.close()
