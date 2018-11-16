from operator import itemgetter

def bin_by_boundaries(column, data, start_bin, size_of_bin, no_of_cols):
    '''Function for data smoothing using binning by boundaries technique'''

    bin_min=data[start_bin][column]
    if start_bin+size_of_bin<no_of_cols:
        bin_max=data[start_bin+size_of_bin][column]
    else:
        bin_max = data[-1][column]
    for each in xrange(start_bin,start_bin+size_of_bin):
        if each<no_of_cols:
            if data[each][column]-bin_min<=bin_max-data[each][column]:
                data[each][column]=bin_min
            else:
                data[each][column]=bin_max
    return data


if __name__ == '__main__':

    f = open("data_imputation.csv", "r")

    f_w = open("data_binning.csv", 'w')

    file_data = f.readlines()

    data=[]

    for each in file_data:
        each=each.split(',')
        each[-1]=each[-1].split('\n')[0]
        each=map(float, each)
        data.append(each)

    size_of_bin=100

    no_of_cols=len(data)

    for each_column in xrange(3,len(data[0])):
        start_bin = 0
        data = sorted(data, key=itemgetter(each_column))
        while start_bin<no_of_cols:
            data=bin_by_boundaries(each_column, data, start_bin, size_of_bin, no_of_cols)
            start_bin=start_bin+size_of_bin

    data=sorted(data, key=itemgetter(1,2))

    for each in data:
        s=','.join(map(str,each))+'\n'
        f_w.write(s)





