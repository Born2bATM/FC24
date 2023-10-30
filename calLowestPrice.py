from itertools import product
import math
import timeit

start = timeit.default_timer()
playersNum = 11
goalStats = 86

def totalStats(listOfStats):
    return sum(listOfStats)

def calStat(listOfStats, playersNum):
    totalStat = sum(listOfStats)
    AvgStat = totalStat / playersNum
    totalBoostPoints = sum(max(0, stat - AvgStat) for stat in listOfStats)
    return math.floor(round(totalStat + totalBoostPoints) / playersNum)

stats = [[84, 85, 86, 87] for _ in range(playersNum)]
price = [[1200, 6000, 11000, 16500] for _ in range(playersNum)]

probStats = list(product(*stats))
probPrice = list(product(*price))

caseStats = []
caseAvgStats = 0
currentMinPrice = float('inf')

for i in range(len(probPrice)):
    p = sum(probPrice[i])
    finalStat = calStat(probStats[i], playersNum)
    
    if finalStat >= goalStats and currentMinPrice > p:
        currentMinPrice = p
        caseAvgStats = finalStat
        caseStats = probStats[i]

print("Total price is", currentMinPrice)
print(caseStats)
print(caseAvgStats)
stop = timeit.default_timer()

print('Time: ', stop - start)