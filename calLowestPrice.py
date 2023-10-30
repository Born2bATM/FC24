

# Python3 code to demonstrate working of
# K Dice Combinations
# Using list comprehension + product()
from itertools import product
import math
 
# initializing K (playersNum)
playersNum = 11
goalStats = 86

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


# Add up your initial, unrounded average player rating to the average points boost.
# using list comprehension to formulate elements

# stats = [list([82,83,84,85,86,87]) for _ in range(playersNum)]
stats = [list([84,85,86,87]) for _ in range(playersNum)]

# price = [list([600,900,2100,6250,11100,17000]) for _ in range(playersNum)]
price = [list([1200,6000,11000,16500]) for _ in range(playersNum)]
 
# using product() to get Combinations
probStats = list(product(*stats))
probPrice = list(product(*price))
totalPrice = list()
caseStats = product()
casePrice = list()
caseAvgStats = 0
currentMinPrice = 999999

for i in range(0,len(probPrice)):
    p = 0
    s = 0
    for j in range(0,playersNum):
        p+=probPrice[i][j]
    finalStat = calStat(probStats[i])
    if finalStat>=goalStats:
        if currentMinPrice > p:
            currentMinPrice = p
            caseAvgStats = finalStat
            caseStats = probStats[i]
        

# printing result

print("Total price is " + str(currentMinPrice))
print(caseStats)
print(caseAvgStats)