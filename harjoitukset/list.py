
import random


furniture = ["table", "chair", "shelf", "sofa"]
print(furniture)
print(furniture[0:2])


for f in furniture:
    if(f == "sofa"):
        print("sofa!")

thrownDiceNumbers = []

for number in range(5):
    thrownDiceNumbers.append(random.randint(1, 6))

print(thrownDiceNumbers)

print("sum: ", sum(thrownDiceNumbers))
print("max: ", max(thrownDiceNumbers))

uniqueNumbers = set()

while(len(uniqueNumbers) < 5):
    uniqueNumbers.add(random.randint(1, 20))

print(uniqueNumbers)