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
    fitness = 0

    #determin fitsness by profits.
    #ensures if the train is late or early it will affect the profits by a certain percentage
    #ensure there is at least 1 of each train car if not that train has 0 profit
    fitness += profits(train) * computeLatence(train) * computeCarRequirment(train) * computeBathRequirment(train) * computeDiningRequirment(train)
    return fitness


def profits(train):
    pass
    profit = 0
    #finds the profit from each passenger by the class type

    #incorporates the actual number of passengers in each class to ensure accurate trains
    #counts the number of each class of passanger cars, calcs actual seats available
    #takes the amount of passangers the train can hold of each class based on availableSeats


    #This is working but could incorporate the actual passanger function 
    numFirstCars = train.count('1')
    availableSeats = numFirstCars * firstPassengers
    actualPassengers = min(numFirst, availableSeats)
    profit += actualPassengers * firstTicket

    numSecondCars = train.count('2')
    availableSeats = numSecondCars * secondPassengers
    actualPassengers = min(numSecond, availableSeats)
    profit += actualPassengers * secondTicket

    numThirdCars = train.count('3')
    availableSeats = numThirdCars * thirdPassengers
    actualPassengers = min(numThird, availableSeats)
    profit += actualPassengers * thirdTicket

    #subtracts the cost of each engine from the profit
    profit -= engineCost*train.count('E')
    return profit


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


#ensures at least 1 of every car exists in the train if not pass 0 so no profit for that train, if all exist pass 1 train is good
def computeCarRequirment(train):
    if ('1' not in train or
        '2' not in train or
        '3' not in train or
        'D' not in train or
        'B' not in train or
        'E' not in train):
        return 0
    return 1


def computeDiningRequirment(train):
    firstPassengers, secondPassengers, thirdPassengers = computeActualPassangers(train)

    numPassangers = firstPassengers + secondPassengers + thirdPassengers 
    numDining = train.count('D')
    actualDining = min(numDining, numPassangers)

    if actualDining < numDining:
        return 0.7
    elif actualDining == numDining:
        return 1
    elif actualDining > numDining:
        return 0.9


def computeBathRequirment(train):
    firstPassengers, secondPassengers, thirdPassengers = computeActualPassangers(train)

    numPassangers = firstPassengers + secondPassengers + thirdPassengers 
    numBath= train.count('B')
    actualBath = min(numBath, numPassangers)

    if actualBath < numBath:
        return 0.7
    elif actualBath == numBath:
        return 1
    elif actualBath > numBath:
        return 0.9
    

#helper function to declutter code to calculate the actual number of passangers possible in a train
def computeActualPassangers(train):
    # First class
    firstCapacity = train.count('1') * firstPassengers
    actualFirst = min(numFirst, firstCapacity)

    # Second class
    secondCapacity = train.count('2') * secondPassengers
    actualSecond = min(numSecond, secondCapacity)

    # Third class
    thirdCapacity = train.count('3') * thirdPassengers
    actualThird = min(numThird, thirdCapacity)

    return actualFirst, actualSecond, actualThird


# 2. selection: Select two individuals from current generation

#simple appaoch where it will grab the first train in the population then compare it to next one in line 
#if number is greater then currrent parent 1 change that train to parent 1
#parent 2 will be the the first train in the population assuming the parent 1 isn't train 1
#then runs the same checks and ensure that parent 2 doesnt equal parent 1
#if it does it skips that train and moves to the next one in population

#after testing and reserch it showd that my generations finished very early in because it always looked at the 2 best parents
#so the only chnage was mutation
#this old parent 2 code is ocmmented out
#new parent 2 code choices a random train in the population that is not parent 1, hopefully adding morer variation to the population

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

    # -------------------------
    # OLD Parent 2 Calculation (Second Best fit parent)
    # -------------------------
    # if parent1 != currentPopulation[0]:
    #     parent2 = currentPopulation[0]
    # else:
    #     parent2 = currentPopulation[1]
    #
    # bestFitness = computeFitness(parent2)
    # for train in currentPopulation:
    #     currentFitness = computeFitness(train)
    #     if train == parent1:
    #         continue
    #     elif currentFitness > bestFitness:
    #         parent2 = train
    #         bestFitness = currentFitness


    # -------------------------
    # NEW Parent 2 (Random, Not Parent 1)
    # -------------------------
    while True:
        parent2 = random.choice(currentPopulation)
        if parent2 != parent1:
            break

    return parent1, parent2


# 3. crossover (takes two individuals and returns one or more 
# individuals created from crossover). You may choose your crossover
# approach
def crossover(train1, train2):
    
    crossover = random.randint(1, trainSize - 1)
    child = train1[:crossover] + train2[crossover:]

    return child

# 4. mutation (takes one individual and returns a possible mutation)
def mutate(train):
    
    mutationChance = 0.2 #change this value to increase or decrease mutation rate
    #check if mutation happens
    if random.random() < mutationChance:
        #random car to mutate
        mutationPoint = random.randint(0, trainSize - 1)
        #random new car to replace it with
        newGene = random.choice(allowedLetters)
        #create new train with mutation
        train = (train[:mutationPoint] + newGene + train[mutationPoint + 1:])
    return train


# 5. create new generation: this function will call the previous
# functions. It should repeatedly select
# a number of pairs and do crossover and mutation on those pairs.
# and it should create a new generation which will be an
# an array of new train strings
def newGeneration(currentPopulation):
    newGeneration = []
    while len(newGeneration) < populationSize:
        #grabs the 2 best parents
        parent1, parent2 = select(currentPopulation)
        #crosses the two best parents to make a child from them
        child = crossover(parent1, parent2)
        #mutates the child to add some variation to the population
        child = mutate(child)
        #adds the child to the new generation
        newGeneration.append(child)

    return newGeneration


###########################
# parameters that can be adjusted 
trainSize=20 #number of cars in the train
populationSize=1000 #number of trains in population
numGenerations=10 #number of generations to run
firstPassengers=10 #number of passengers a first class car carries
secondPassengers=24 #number of passengers a second class car carries
thirdPassengers=50 #number of passengers a third class car carries

#ticket prices for each class
firstTicket=1500
secondTicket=500
thirdTicket=200
#price per engine
engineCost=15000

# for now make these a multiple of the number of passengers a car will hold 
numFirst=firstPassengers*10
numSecond=secondPassengers*12
numThird=thirdPassengers*20


#Num of passangers each car can serve
numDining = 30
numBath = 20

currentPopulation=generateInitialPopulation()
printTrain(currentPopulation[0])
for i in range(numGenerations):
    currentPopulation=newGeneration(currentPopulation)
    best = max(currentPopulation, key=computeFitness)
    print("Best fitness:", computeFitness(best))
    printTrain(best)
