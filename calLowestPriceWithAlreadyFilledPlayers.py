

# Python3 code to demonstrate working of
# K Dice Combinations
# Using list comprehension + product()
from itertools import product
 
# initializing K
K = 11
goalStats = 82.5
alreadyFilled = list([83,80,81,79,82])
totalStats = 0
remainingK = 11-len(alreadyFilled)
 
for i in range(0,len(alreadyFilled)):
    totalStats+=alreadyFilled[i]


stats = [list([82,83,84,85]) for _ in range(remainingK)]
price = [list([600,900,2100,6250]) for _ in range(remainingK)]

# using product() to get Combinations
probStats = list(product(*stats))
probPrice = list(product(*price))
totalPrice = list()
caseStats = list()
casePrice = list()
caseAvgStats = list()

for i in range(0,len(probPrice)):
    p = 0
    s = 0
    for j in range(0,remainingK):
        p+=probPrice[i][j]
        s+=probStats[i][j]
    if (s+totalStats)/K>=goalStats:
        caseAvgStats.append((s+totalStats)/K);
        totalPrice.append(p);
        caseStats.append(probStats[i])
        casePrice.append(probPrice[i])

# printing result

print("Total price is " + str(min(totalPrice)))
print(caseStats[totalPrice.index(min(totalPrice))])
print(caseAvgStats[totalPrice.index(min(totalPrice))])


#print result
print(totalStats)