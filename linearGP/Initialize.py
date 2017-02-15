import Preprocess
import random
#population, N > 4
N = 50

#instruction number in one individual
X = 8

#produce instrucitons:
#0:+,1:-,2:*,3:/
#mode 0: read from register, 1: read from input
#instruction list: [target,opcode,source,mode]

def produce_instrucion ():
    instructionlist = []
    for i in range(X):
        templist = []
        for j in range(3):
            templist.append(random.randrange(0,4))
        templist.append(random.randrange(0,2))
        instructionlist.append(templist)
    return instructionlist


population = []
for i in range(N):
    population.append(produce_instrucion())

#print (population[0])

#if __name__ == '__main__':