

# Python3 code to demonstrate working of
# K Dice Combinations
# Using list comprehension + product()
from itertools import product
 
# initializing K
K = 11
goalStats = 85.5
 
# using list comprehension to formulate elements
# stats = [list([82,83,84,85,86,87]) for _ in range(K)]
stats = [list([85,86,87]) for _ in range(K)]

# price = [list([600,900,2100,6250,11100,17000]) for _ in range(K)]
price = [list([6250,11100,17000]) for _ in range(K)]
 
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
    for j in range(0,K):
        p+=probPrice[i][j]
        s+=probStats[i][j]
    if s/K>=goalStats:
        caseAvgStats.append(s/K);
        totalPrice.append(p);
        caseStats.append(probStats[i])
        casePrice.append(probPrice[i])

# printing result

print("Total price is " + str(min(totalPrice)))
print(caseStats[totalPrice.index(min(totalPrice))])
print(caseAvgStats[totalPrice.index(min(totalPrice))])