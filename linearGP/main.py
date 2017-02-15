import Initialize
import Preprocess
import SSTreplace
import PSreplace
import random
import Fitnesscaculate

Best = 0.8
G = 100

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
#randomly choose replace method
        replacemethod = random.randrange(0,2)
        if replacemethod == 0 :
            population = SSTreplace.SSTreplace(population,trainlist)
        elif replacemethod == 1 :
            population = PSreplace.PSreplace(population, trainlist)

maxfitness_all_genetration = max(max_fitness_list)
maxindex_all_genetration = max_fitness_list.index(maxfitness_all_genetration)
maxfitness_all_genetration_test = max_finess_test_list[maxindex_all_genetration]

print('Best fitness of training list is No.',maxindex_all_genetration,'train fitness:',maxfitness_all_genetration,'test fitness :',maxfitness_all_genetration_test)

