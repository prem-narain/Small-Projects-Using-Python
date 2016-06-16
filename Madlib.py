import random
# Open the madlibs text file
f = open('libs.txt','r')
allLines = f.readlines()
# Choose a random madlib from the list
madlib = random.choice(allLines)
# Separate the input list from the story
halves = madlib.split("#")
# The second item is the madlib text
madlibText = halves[1]
# Now get the inputs required one by one
inputs = halves[0].split(",")
inputStore = [""]
for item in inputs:
    inputStore.append(input("Enter a "+item+": "))
# Print out the madlib but replace the markers with the inputs
for i in range(len(inputStore)):
    madlibText = madlibText.replace("%"+str(i), inputStore[i])
# Get rid of whitespace (this annoys me)
madlibText = madlibText.strip()
print (madlibText)
