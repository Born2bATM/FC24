

# Python3 code to demonstrate working of
# K Dice Combinations
# Using list comprehension + product()
from itertools import product
import math
 
# initializing K
playersNum = 11
goalStats = 85
alreadyFilled = list([84,83,84,84,82,85])
totalStats = 0
remainingPlayersNum = playersNum-len(alreadyFilled)

def totalStats(listOfStats):
    totalStats=0
    for i in range(0,len(listOfStats)):
        totalStats+=listOfStats[i]
    return totalStats

def calStat(listOfStats):
    totalStat = totalStats(listOfStats)
    AvgStat = totalStat/playersNum
    totalBoostPoints=0
    for i in range(0,len(listOfStats)):
        if(listOfStats[i]>AvgStat):
            totalBoostPoints += (listOfStats[i]-AvgStat)
    return math.floor(round(totalStat+totalBoostPoints)/11)

stats = [list([82,83,84,85,86]) for _ in range(remainingPlayersNum)]
price = [list([600,900,2100,6250,11000]) for _ in range(remainingPlayersNum)]

# using product() to get Combinations
probStats = list(product(*stats))
probPrice = list(product(*price))
totalPrice = list()
caseStats = list()
casePrice = list()
caseAvgStats = list()

for i in range(0,len(probPrice)):
    p = 0
    for j in range(0,remainingPlayersNum):
        p+=probPrice[i][j]
    tempList = list(probStats[i])
    for k in range(0,len(alreadyFilled)):
        tempList.append(alreadyFilled[k])
    finalStat = calStat(tempList)
    if finalStat>=goalStats:
        caseAvgStats.append(finalStat);
        totalPrice.append(p);
        caseStats.append(probStats[i])
        casePrice.append(probPrice[i])
    tempList.clear()

# printing result

print("Total price is " + str(min(totalPrice)))
print(caseStats[totalPrice.index(min(totalPrice))])
print(caseAvgStats[totalPrice.index(min(totalPrice))])
