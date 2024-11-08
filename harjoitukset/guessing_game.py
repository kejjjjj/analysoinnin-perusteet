
NAME = "testi"
numGuesses = 0
numHints = 0

while(1):
    value = input("Please, guess my name: ")
    numGuesses += 1
    
    if(len(value) > 0 and value == NAME):
        print("Congratulations!")
        break

    numHints += 1
    print("Hint: ", NAME[0:min(numHints, len(NAME))])


print("Guesses", numGuesses)