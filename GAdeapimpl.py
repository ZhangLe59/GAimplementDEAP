import random
from deap import creator, base, tools, algorithms

listinput = []
def startalgrithm(topk):
    liststring = input("pls input the list, saperate with , :")
    for item in liststring.split(','):
        listinput.append(int(item))
    creator.create("FitnessMax", base.Fitness, weights=(1,))  #weights 
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, -1, 1) # value range
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(listinput)) #number of parameters
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evalOneMax)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    population = toolbox.population(n=300)
    NGEN=40
    for gen in range(NGEN):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=len(population))
    topk = input("pls input the number of result:")
    top2 = tools.selBest(population, k=int(topk))  #top1
    return top2

def evalOneMax(individual):
    #return sum(individual),
    #listinput = [3,2,9,2,7,5]
    listbuy = []
    sumcount = 0
    for index,item in enumerate(listinput):
        if(individual[index] == 1):
            listbuy.append(item)
            sumcount = sumcount - item
        if(individual[index] == -1):
            for itemsub in listbuy:
                sumcount = sumcount + item
            listbuy = [] 
        #print(individual,sumcount)     
    return sumcount,

print(startalgrithm(3))
