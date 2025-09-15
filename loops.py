# For Loops in Python
listOfPuppies = ['Guts', 'Ace', 'Sammie']
for thisPuppy in listOfPuppies:
    print(f'My favorite puppy is {thisPuppy}!!!')

# Looping Through a String
name = 'RufusXavierSarsaparilla'
nameLength = 0
for letter in name:
    print(letter)
    nameLength += 1
print(f'Name is {nameLength} letters long.')

# Break Statement
planets = ['Tatooine', 'Yavin IV', 'Alderaan']
rebelBase = 'Alderaan'
target = 'none'
for thisPlanet in planets:
    if thisPlanet == rebelBase:
        target = thisPlanet
        break
print(f"Firing lasers at {target}!")

# Continue Statement
wordList = ['toast', 'boat', 'jam', 'do', 'a', 'antidisestablishmentarianism']
wordLengthLimit = 4
longWords = shortWords = 0
for thisWord in wordList:
    if thisWord.__len__ <= wordLengthLimit:
        shortWords += 1
        continue
    else:
        longWords += 1
        print(f"Long word detected: {thisWord}!")
print(f"Found {longWords} long words!")

# Range
tickets = 6
for nowServing in range(tickets):
    print(f"Now serving ticket #{nowServing+1}!")

# Range Start and End
startYear = 1989
endYear = 2001
for thisYear in range(startYear, endYear):
    print(f"The year is {thisYear} and nothing has changed.")

# Else in For
listOfPeople = ['Big Boss', 'Solid Snake', 'Revolver Ocelot', "Liquid Snake"]
for checkIdentity in listOfPeople:
    print(f"Checking identity. Subject Found: {checkIdentity}")
    if 'Snake' in checkIdentity:
        print("SNAAAAAAKE!")
        break
else:
    print("All clear! No snake here.")

# Nested Loops
listOfCars = ['Viper', 'Miata', 'Veloster']
listOfParts = ['Engine', 'Exhaust', 'Suspension']
for thisCar in listOfCars:
    for thisPart in listOfParts:
        print(f"Wow, check out the {thisPart} on that {thisCar}!")

# Pass
sleepyHeads = ['Kitty', 'Puppy', 'Baby']
shouldNotWakeSleepyHeads = True
for thisSleepyHead in sleepyHeads:
    if shouldNotWakeSleepyHeads:
        pass
    else:
        print(f"Hey sleepy head {thisSleepyHead}, wake up!")
