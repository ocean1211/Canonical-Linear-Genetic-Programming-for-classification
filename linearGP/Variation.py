import random

def crossover(list1,list2):
    a = len(list1)
    b = len(list2)
    if not a == b:
        error = 'Instruction lenth error'
        return error
    start = random.randrange(0,a)
    depth = random.randrange(1,a-start+1)
    end = start+depth
    templist = list1[start:end]
    list1[start:end] = list2[start:end]
    list2[start:end] = templist
    result =[list1,list2]
    return result

def mutation(instrutionlist):
    listlen = len(instrutionlist)
    instructionlen = len(instrutionlist[0])
    # print('listlen =',listlen)
    # print('nstructionlen =', instructionlen)
    mutateinstrution = random.randrange(0,listlen)
    mutatetimes = random.randrange(1,instructionlen+1)

    for i in range(mutatetimes):
        mutatepoint = random.randrange(0,instructionlen)
        #print('point = ',mutatepoint)
        if (mutatepoint < 3):
            mutatevalue = random.randrange(0,4)
        elif (mutatepoint == 3):
            mutatevalue = random.randrange(0, 2)
        instrutionlist[mutateinstrution][mutatepoint] = mutatevalue
    return(instrutionlist)

#randomly decide order of crossover and mutation
#0:crossover first,1: mutate first
def variation (list1,list2):
    order = random.randrange(0, 2)
    result = []
    if (order == 0):
        newlists = crossover(list1,list2)
        result.append(mutation(newlists[0]))
        result.append(mutation(newlists[1]))
        #print ('result',result)

    elif(order == 1):
        #print('list1',list1)
        list1 = mutation(list1)
        list2 = mutation(list2)
        result = crossover(list1,list2)
        #print('result =', result)
    return result







