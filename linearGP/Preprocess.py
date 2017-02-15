#fitness function: fitness is the number of successful test

import numpy
import random
import itertools

Scale = 10

file = open ('iris.data.txt')
orgdata = []
for line in file:
    str = line.strip()
    if not (str == ''):
        orgdata.append(str.split(','))
datalist = []
varlist = []
meanlist = []
standlist = []
testlist = []
trainlist = []

N = len(orgdata)

#standlization
for j in range(len(orgdata[0])-1):
    templist = []
    for i in range(len(orgdata)):

# if attribute is letter, change it to ASCII then change ASCII code to smaller interger
        if (orgdata[i][j].isalpha()):
            templist.append(ord(orgdata[i][j])%(len(orgdata[0])-1))
        else:
            templist.append(round(float(orgdata[i][j]), 2))
    datalist.append(templist)
    narray = numpy.array(datalist[j])
    mean = numpy.mean(narray)
    var = numpy.var(narray)
    varlist.append(var)
    meanlist.append(mean)


for j in range(len(orgdata[0])-1):
    templist = []
    for i in range (len(orgdata)):
        templist.append(Scale*(datalist[j][i] - meanlist[j]) / varlist[j])
    standlist.append(templist)

templist = []
for i in range(len(orgdata)):
    templist.append(orgdata[i][j+1])
standlist.append(templist)
datalist.append(templist)


#choose 80 percent as training set according to class distribution, lest 20 percent as test set
classlist = list(set(datalist[len(orgdata[0])-1]))
classlist.sort(key=datalist[len(datalist)-1].index)
classnumber = len (classlist)

classconsist = []
for i in range(classnumber):
    classconsist.append(datalist[len(orgdata[0])-1].count(classlist[i]))

randomlist = []
for i in range(classnumber):
    randomlist.append(random.sample(range(classconsist[i]),int(0.8*classconsist[i])))
    randomlist[i].sort()

#print(randomlist)

addnumber = 0
for i in range(classnumber-1):
    addnumber = addnumber + classconsist[i]
    for j in range(len(randomlist[i+1])):
        randomlist[i+1][j] = randomlist[i+1][j]+addnumber
randomlist = list(itertools.chain.from_iterable(randomlist))



for i in range(len(orgdata[0])):
    templist = []
    for j in range(len(randomlist)):
        templist.append(standlist[i][int(randomlist[j])])
    trainlist.append(templist)



testlistID = list(set(range(len(orgdata))).difference(set(randomlist)))
testlistID.sort()


for i in range(len(orgdata[0])):
    templist = []
    for j in range(len(testlistID)):
        templist.append(standlist[i][int(testlistID[j])])
    testlist.append(templist)
