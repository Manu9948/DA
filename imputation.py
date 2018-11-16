import math
import sys

def distance(missing_row, other_row):
    '''Function which is used to calculate the distance between two points'''
    d=0
    for each_feature in xrange(len(other_row)):
        if ''!=missing_row[each_feature] and ''!=other_row[each_feature]:
            temp=abs(float(missing_row[each_feature])-float(other_row[each_feature]))
            d=d+temp*temp
    return math.sqrt(d)

def imputation(index, data):
    '''Function which is used to find the nearest point for the given point'''
    min_dis=sys.maxsize
    min_index=-1
    for each_row in xrange(len(data)):
        if index!=each_row and '' not in data[each_row]:
            d=distance(data[index],data[each_row])
            if min_dis>d:
                min_index=each_row
                min_dis=d
    return min_index

def replace(index, nearest, data):
    '''Function which is used to replace the missing values using imputation technique'''
    for each in xrange(len(data[nearest])):
        if data[index][each]=='':
            data[index][each]=data[nearest][each]
    return data

if __name__ == '__main__':

    f = open("/Users/manohar/Documents/Projects/DA/dengue/datasets/dengue_features_train.csv", "r")

    f_w = open("data_imputation.csv", 'w')

    file_data = f.readlines()[1:]

    data=[]

    for each in file_data:
        each = each.split(',')
        each[-1]=each[-1].split("\n")[0]
        each.pop(3)
        if each[0]=='sj':
            each.pop(0)
            each.insert(0,0)
        else:
            each.pop(0)
            each.insert(0,1)
        data.append(each)


    for index in xrange(len(data)):
        if '' in data[index]:
            nearest=imputation(index, data)
            data=replace(index, nearest, data)

    for each in data:
        s=','.join(map(str,each))+'\n'
        f_w.write(s)


