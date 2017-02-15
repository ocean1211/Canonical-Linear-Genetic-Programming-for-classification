import Initialize
import random
import Fitnesscaculate
import Preprocess
import itertools
import Variation

# Generation
G = 100
#stop if fitness (max = 1) arrirves at Best
Best = 0.8

# find the pair of indivudals of specific fitness propotion
def find_parents(parents,fitness_propotion_sort):
    parents_real_propotion = [-1,-1]
    for i in fitness_propotion_sort:
        if i >= parents[1]:
            parents_real_propotion[1] = i
            if (parents_real_propotion[0] == -1):
                parents_real_propotion[0] = i
            return parents_real_propotion

        elif i >= parents[0] and i < parents[1] and parents_real_propotion[0] == -1:
            parents_real_propotion[0] = i



def PSreplace (population,trainlist):
    populationsize = len(population)
    fitnesslist = []
    for i in range(populationsize):
        testinstruction = population[i]
        # print('testinstruction = ',testinstruction)
        fitness = Fitnesscaculate.implement_operation(testinstruction, trainlist)
        fitnesslist.append(fitness)
    fitness_sum = sum(fitnesslist)
    fitness_propotion = []

#caculate fitness propotion
    for i in range(len(fitnesslist)):
        if (fitness_sum == 0):
            fitness_propotion.append(0)
        else:
            fitness_propotion.append(fitnesslist[i]/fitness_sum)

#select by propotion
    fitness_propotion_sort = sorted(fitness_propotion)

    max_fitness_propotion = max(fitness_propotion_sort)
    parent_propotion_list = []
    parents_list = []

    for i in range(int(populationsize/2)):
#randomly select propotion
        parents = [random.uniform(0,max_fitness_propotion),random.uniform(0,max_fitness_propotion)]
        parents.sort()
        parent_propotion_list.append(parents)

        parents_propotion_value = find_parents(parents,fitness_propotion_sort)

# if selected propotion has more than one individual, randomly select one
        parents_index = [[j for j, v in enumerate(fitness_propotion) if v == parents_propotion_value[0]] , [j for j, v in enumerate(fitness_propotion) if v == parents_propotion_value[1]]]
        if len(parents_index[0]) > 1:
            parents_index[0] = random.sample(parents_index[0],1)
        if len(parents_index[1]) > 1:
            parents_index[1] = random.sample(parents_index[1], 1)
        parents_index = list(itertools.chain.from_iterable(parents_index))
        parents_list.append([population[parents_index[0]],population[parents_index[1]]])


    children_list = []
    for i in range(len(parents_list)):
        child = Variation.variation(parents_list[i][0], parents_list[i][1])
        children_list.append(child[0])
        children_list.append(child[1])

    population = children_list

    #print('parent list ',parents_list)

    return population

#caculate fitness and return maxfitness
def caculate_population_fitness(population,datalist):
    fitnesslist = []
    for i in range(len(population)):
        testinstruction = population[i]
        fitness = Fitnesscaculate.implement_operation(testinstruction, datalist)
        fitnesslist.append(fitness)
    largestfitness = max(fitnesslist)
    maxindex = fitnesslist.index(largestfitness)

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
            maxfitness_trainlist = caculate_population_fitness(population,trainlist)
            maxindex = maxfitness_trainlist[1]
            fitness_trainlist = round(maxfitness_trainlist[0]/len(trainlist[0]),3)
            max_fitness_list.append(fitness_trainlist)
            fitness_testlist = caculate_population_fitness([population[maxindex]],testlist)
            max_finess_test_list.append(round(fitness_testlist[0]/len(testlist[0]),3))
            print('No.',i,'Generation ','train fitness:',fitness_trainlist,'; test fitness:',round(fitness_testlist[0]/len(testlist[0]),3))
            population = PSreplace(population,trainlist)


    maxfitness_all_genetration = max(max_fitness_list)
    maxindex_all_genetration = max_fitness_list.index(maxfitness_all_genetration)
    maxfitness_all_genetration_test = max_finess_test_list[maxindex_all_genetration]
    print('Best fitness of training list is No.',maxindex_all_genetration,'train fitness:',maxfitness_all_genetration,'test fitness :',maxfitness_all_genetration_test)



