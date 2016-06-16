import random
def Diceroll():
    min = 1
    max = 6
    Rolling = "yes"

    while Rolling== "yes" or Rolling == "y":
        print ("Rolling the dices...")
        print ("The values are....")
        print (random.randint(min, max))
        Rolling = raw_input("Roll the dices again?")

Diceroll()
