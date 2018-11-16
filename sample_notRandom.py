import random




f=open('data_binning.csv','r')
data=f.readlines()
f.close()


def findRandomData(data):
    for _ in range(len(data)):
        num= random.randint(0,len(data))
        if num not in number:
            return data[number]


def findData(data, mean , direction):

    for _ in  range(len(data)):
        num = random.randint(0, len(data)-1)
        try:
            if num not in number:
                if direction and findAB(data[num].split(',') ,mean) :
                    return data[num]
                if direction ==False and findAB(data[num].split(',') ,mean) == False:
                    return data[num]
        except Exception as e:
            print num , len(data)
            print e
            exit()
    return None



def findAB(a,b):
    count=0
    for i in range(len(a)):
        if float(a[i]) > b[i]:
            count= count +1
    if count > len(a)/2 :
        return True
    else:
        return False


def findUpDown(data,mean):
    count=0
    for line in data:
        if findAB(line.split(','),mean):
            count= count+1
    if count > len(data)/2 :
        return True
    else:
        return False




def findmean(data):
    n= len(data)
    mean=[]
    for _ in range(len(data[0].split(","))):
        mean.append(0)

    for line in data:
        line= line.split(",")
        for i in range(len(line)):
            if i == len(line)-1:
                mean[i] = mean[i] + float(line[i].split('\n')[0])
            else:
                mean[i]=mean[i]+float(line[i])


    for i in range(len(data[0].split(","))):
        mean[i] =mean[i]/n

    return mean


number=[]
newData=[]
length = 0.1*len(data)
i=0

for _ in range(len(data)):

    if i >= 3:
        break
    num=random.randint(0,len(data))
    if num not in number:
        newData.append(data[num])
        number.append(num)
        i=i+1

#print "data lenght ", len(data[0])

#print newData
#print "new Data length" , len(newData[1])

for _ in range(len(data)):

    if i > length:
        break
    mean = findmean(newData)
    #print mean
    #print "mean lenght "  , len(mean)
    temp=findUpDown(newData,mean)
    temp_data=findData(data,mean,temp)
    #print temp_data , temp
    if temp_data == None:
        temp_data=findRandomData(data)

    newData.append(temp_data)
    #print newData
    i=i+1

f=open('sample_notRandom.csv','w')
for line in newData:
    f.write(line)

f.close()