import random
import numpy
import gini

class Actor:
    def __init__(self, id, funds):
        self.name = id
        self.funds = funds

    def __str__(self):
        return "Actor: {} has {}\n".format(self.name, self.funds)

def encounter(a, b, tradePercentage = 0.05):
    value =  min(a.funds, b.funds)*tradePercentage

    winnerIndex = random.randrange(1)
    if winnerIndex == 0:
        a.funds = a.funds + value
        b.funds = b.funds - value
    else:
        b.funds = b.funds + value
        a.funds = a.funds - value

    

def displayStats(all, detail):
    maxFunds = max(all)
    print(numpy.histogram(all,bins = detail, range=(0, maxFunds))[0])
    print("max funds: ", maxFunds)
    
if __name__ == "__main__":
    #text for gittest
    numActors = 1000
    startFunds = 1000
    allActors = {}
    for i in range(numActors):
        allActors[i] = Actor(i, startFunds)

    
    for encounters in range(1000000):
        id1 = random.randrange(numActors)
        id2 = random.randrange(numActors)
        if id1 != id2:
            encounter(allActors[id1], allActors[id2])

    funds = [a.funds for a in allActors.values()] 
    displayStats(funds, 20)
    funds.sort()
    print(funds[0:10])
    gini.showGini(numpy.array(funds))
