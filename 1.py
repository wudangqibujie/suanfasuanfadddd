import numpy as np
import math
class KNN():
    def __init__(self):
        pass
    def data_import(self,filename):
        f = open(filename)
        data = []
        labels = []
        for i in f:
            b = i.strip().split("\t")  #
            b[0] = int(b[0])
            # print(repr(b[0]))
            b[1] = float(b[1])
            b[2] = float(b[2])
            data.append(b[:3])
            labels.append(b[3])

        data1 = np.array(data)
        # print(data1)
        return data1,labels

    def two_distance(self,seq1,seq2):
        a = (seq1-seq2)**2
        b = np.sum(a)
        distance = np.sqrt(b)
        return distance



if __name__ == '__main__':
    rr = KNN()
    data1,labels= rr.data_import("datingTestSet.txt")
    data2,label = rr.data_import("test.txt")
    # print(data1)
    # print(data2)
    # dis = rr.two_distance(data2[0, :3], data1[0, :3])
    # print(label)
    # print(data1.shape)
    # print(data2.shape)
    distan = []
    for i in range(1000):
        dis = rr.two_distance(data2[0,:3],data1[i,:3])
        distan.append(dis)


    ii = distan.index(min(distan))
    result = labels[ii]
    print(result)

        # dd[labels[i]] = dis
        # print(dis,labels[i])


    # print(type(dis))
    # print(dd)

    #
    #
    # print(data1[0,:])
    # print(data2[0,:])
    # dis = rr.two_distance(data2[0,:],data1[0,:])
    # print(dis)





