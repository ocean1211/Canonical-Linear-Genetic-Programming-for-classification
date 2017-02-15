import Initialize
import random
import Fitnesscaculate
import heapq
import Preprocess
import itertools
import Variation


#number of parents， N%4 == 0
N = 4
#number of genetration
G = 100
#stop if fitness (max = 1) arrirves at Best
Best = 0.8

def SSTreplace (population,trainlist):
    populationsize = len(population)
    # for i in population:
    #     print(i)

    parentlist = random.sample(range(populationsize),N)
    # print('parentlist = ',parentlist)
    fitnesslist = []
    for i in range(N):
        testinstruction = population[parentlist[i]]
        #print('testinstruction = ',testinstruction)
        fitness = Fitnesscaculate.implement_operation(testinstruction,trainlist)
        fitnesslist.append(fitness)
    #print('fitnesslist = ',fitnesslist)
    largestfitness = max(fitnesslist)

    largerfitness = heapq.nlargest(int(N/2),fitnesslist)
    #print(largerfitness)
    number_larger_value = list(set(largerfitness))
    #print('number =', number_larger_value)

    larger_value_count = []
    for i in range(len(number_larger_value)):
        largercount = largerfitness.count(number_larger_value[i])
        larger_value_count.append([number_larger_value[i],largercount])

    largerindex = []
    largerlist = []
    for i in range(len(larger_value_count)):
        larger_temp_index = [j for j, v in enumerate(fitnesslist) if v == larger_value_count[i][0]]
        temp = random.sample(larger_temp_index, larger_value_count[i][1])
        largerindex.append(temp)

    largerindex = list(itertools.chain.from_iterable(largerindex))

    for i in range(len(largerindex)):
        largerlist.append(parentlist[largerindex[i]])

# individuals to be replaced
    smallerlist = list(set(parentlist).difference(set(largerlist)))
    smallerlist.sort()
    # print('samller = ',smallerlist)
    parentpairs = [largerlist[i:i+2] for i in range(0,int(N/2),2)]
    #print(parentpairs)

    childrenlist =[]

    for i in range(len(parentpairs)):
        instruction1 = population[parentpairs[i][0]]
        #print('ins1 =',instruction1)
        instruction2 = population[parentpairs[i][1]]
        #print('ins2 =', instruction2)
        child = Variation.variation(instruction1,instruction2)
        #print('child = ',child)
        childrenlist.append(child[0])
        childrenlist.append(child[1])

    for i in range(len(smallerlist)):
        population[smallerlist[i]] = childrenlist[i]

    # for i in population:
    #     print(i)
    # for i in childrenlist:
    #     print(i)
    return population

def caculate_population_fitness(population,datalist):
    fitnesslist = []
    for i in range(len(population)):
        testinstruction = population[i]
        fitness = Fitnesscaculate.implement_operation(testinstruction, datalist)
        fitnesslist.append(fitness)
    largestfitness = max(fitnesslist)
    maxindex = fitnesslist.index(largestfitness)
    #print(largestfitness)
    #print(maxindex)
    return [largestfitness,maxindex]

if __name__ == '__main__':

    population = Initialize.population
    trainlist = Preprocess.trainlist
    testlist = Preprocess.testlist

    fitness_trainlist = 0
    max_fitness_list = []
    max_finess_test_list = []

    print(' number in training: ',len(trainlist[0]),'number in testing : ',len(testlist[0]))

    for i in range (G):
        if (fitness_trainlist < Best):

    #get max fitness in population with training list
            maxfitness_trainlist = caculate_population_fitness(population,trainlist)
            maxindex = maxfitness_trainlist[1]
            fitness_trainlist = round(maxfitness_trainlist[0]/len(trainlist[0]),3)
            max_fitness_list.append(fitness_trainlist)

    #get counter fitness with test list
            fitness_testlist = caculate_population_fitness([population[maxindex]],testlist)
            max_finess_test_list.append(round(fitness_testlist[0]/len(testlist[0]),3))
            print('No.',i,'Generation ','train fitness:',fitness_trainlist,'; test fitness:',round(fitness_testlist[0]/len(testlist[0]),3))
            population = SSTreplace(population,trainlist)


    maxfitness_all_genetration = max(max_fitness_list)
    maxindex_all_genetration = max_fitness_list.index(maxfitness_all_genetration)
    maxfitness_all_genetration_test = max_finess_test_list[maxindex_all_genetration]

    print('Best fitness of training list is No.',maxindex_all_genetration,'train fitness:',maxfitness_all_genetration,'test fitness :',maxfitness_all_genetration_test)







