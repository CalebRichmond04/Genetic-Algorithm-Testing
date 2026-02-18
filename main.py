import random

allowedLetters="123DBE"


def generateInitialPopulation():
    currentPopulation=[]
    w=[1,1,1,1,1,1] #weights for each code.
    for i in range(populationSize):
        train= ''.join(random.choices(allowedLetters,weights=w, k=trainSize))
        #print(train)
        currentPopulation.append(train)
    return currentPopulation

def printTrain(train):
    names={'1':'First','2':'Second','3':'Third','E':'Engine','D':'Dining','B':'Bathroom'}
    #join the name for each character, separated by a -
    string='-'.join(names[c] for c in train)
    print(string)

###############Functions you will write ###########

# 1. compute fitness of solution.
def computeFitness(train):
    pass

    #determin fitsness by profits.
    #ensures if the train is late or early it will affect the profits by a certain percentage
    #if no engine exists no profits can be made because the train cant move
    return profits(train) * computeLatence(train)

def profits(train):
    pass
    profit = 0
    #finds the profit from each passenger by the class type
    #incorporate the actual number of passengers in each class to make it more accurate
    for i in train:
        if i == '1':
            profit += firstTicket * (firstPassengers)
        elif i == '2':
            profit += secondTicket * (secondPassengers) 
        elif i == '3':
            profit += thirdTicket * (thirdPassengers)
    #subtracts the cost of each engine from the profit
    profit -= engineCost*train.count('E')
    return profit

#if engine less than requried late by 10 minuets
#if egnine more than requried early by 10 minuets
def computeLatence(train):
    pass
    timeliness = 0
    numEngine = 0
    requiredEngine = trainSize // 20
#finds number of engines in the train
    for i in train:
        if i == 'E':
            numEngine += 1
#checks if the number of engines is less than, greater than, or equal to the required number of engines
    #if number of engines is less than train cant move so timeliness is 0 making profits 0
    if numEngine == 0:
        timeliness = 0
    #if number of engines is less than required profits decrease by 10% because of lateness
    elif numEngine < requiredEngine:
        timeliness = 0.9
    #if number of engines is equal to required engines profits stay the same
    elif numEngine == requiredEngine:
        timeliness = 1.0   
    #if number of engines is more than profits increase by 10% because of earliness
    #change number to something less than 1.1 as algorithm could prioritize more engines 
    #if engine price is increased it might not matter as much but it could still be an issue
    elif numEngine > requiredEngine:
        timeliness = 1.1
    return timeliness




# 2. selection: Select two individuals from current generation
#simple appaoch where it will grab the first train in the population then compare it to next one in line 
#if number is greater then currrent parent 1 change that train to parent 1
#parent 2 will be the the first train in the population assuming the parent 1 still insent train 1
#then runs the same checks and ensure that parent 2 doesnt equal parent 1
#if it does it skips that train and moves to the next one in population
def select(currentPopulation):
    pass
#parent 1 calc
    parent1 = currentPopulation[0]
    bestFitness = computeFitness(parent1)
    for train in currentPopulation:
        currentFitness = computeFitness(train)
        if currentFitness > bestFitness:
            parent1 = train
            bestFitness = currentFitness

#parent 2 calc



# 3. crossover (takes two individuals and returns one or more 
# individuals created from crossover). You may choose your crossover
# approach
def crossover(train1, train2):
    pass

# 4. mutation (takes one individual and returns a possible mutation)
def mutate(train):
    pass

# 5. create new generation: this function will call the previous
# functions. It should repeatedly select
# a number of pairs and do crossover and mutation on those pairs.
# and it should create a new generation which will be an
# an array of new train strings
def newGeneration(currentPopulation):
    pass


###########################
# parameters that can be adjusted 
trainSize=20 #number of cars in the train
populationSize=1000 #number of trains in population
numGenerations=1 #number of generations to run
firstPassengers=10 #number of passengers a first class car carries
secondPassengers=24 #number of passengers a second class car carries
thirdPassengers=50 #number of passengers a third class car carries

#ticket prices for each class
firstTicket=1500
secondTicket=500
thirdTicket=200
#price per engine
engineCost=1500

# for now make these a multiple of the number of passengers a car will hold 
numFirst=firstPassengers*10
numSecond=secondPassengers*12
numThird=thirdPassengers*20

currentPopulation=generateInitialPopulation()
printTrain(currentPopulation[0])
for i in range(numGenerations):
    currentPopulation=newGeneration(currentPopulation)
