# Define a function

def sayHello():
    print("Hello there!")


sayHello()


# Function definitions can have parameters


def introduce(name):
    print(f"This is {name}")


introduce("Me")


def makeSandwich(filling, wrapper):
    print(f"You made a {filling} sandwich with a {wrapper} wrapper")


makeSandwich("Peanut Butter", "Cracker")

# Invoke a function
sayHello()
sayHello()
sayHello()
# sayHello("You") # Error: Wrong number of arguments

introduce("Guybrush Threepwood")
introduce("Largo LaGrande")
introduce("Governer Marley")
# introduce("Carla", "Otis", "Meathook") # Error: Wrong number of arguments

makeSandwich("Tofu", "Pita")
makeSandwich("Hot Dog", "Bun")
makeSandwich("Pancake", "Pancake")
# makeSandwich("Pancake", "Pancake", "Toast") # Error: Wrong number of arguments

# Parameters vs Arguments


def negotiateTerms(aGoodReason, theMeansToDoIt):  # Parameters
    print(f"{aGoodReason+theMeansToDoIt}")


negotiateTerms("Here's Why", "You Can Do It")  # Arguments

# Arbitrary Args


def talkAboutMyFavoriteDogs(*dogs):
    for thisDog in dogs:
        print(f"My favorite dog is {thisDog}")


talkAboutMyFavoriteDogs("Guts", "Ace", "Sammie")  # 3
talkAboutMyFavoriteDogs("River", "Cadence")  # 2
talkAboutMyFavoriteDogs()  # Still works

# Keyword Arguments


def orderOfThings(first, middle, last):
    print(f"First you {first}, then you {middle}, finally you {last}")


orderOfThings(last="LastThing", middle="MiddleThing", first="FirstThing")


# Arbitrary Keywords
def fitCheck(**gear):
    print(f"Hat: {gear["hat"]}")
    print(f"Jacket: {gear["jacket"]}")
    print(f"Shoes: {gear["shoes"]}")


fitCheck(shoes="Zero Drop", jacket="Zippy", hat="Tinfoil")
# fitCheck(hat="Propeller",shoes="Bowling") # Error: Missing Keyword
# fitCheck(jacket="Long")  # Error: Missing Keyword

# Default Parameter Values


def addPizzaTopping(topping="pineapple"):
    print(f"Added {topping} to pizza")


addPizzaTopping()
addPizzaTopping("olives")

# List as Argument


def trickOrTreat(candyList):
    for thisCandy in candyList:
        print(f"Here's your candy: {thisCandy}")


candies = ['Rollos', 'M+Ms', 'Sour Gummy Worms']
trickOrTreat(candies)

# Return Values


def makeItWeird(oldWord):
    return oldWord.swapcase().zfill(18)


print(f"A weird word: {makeItWeird("Toast Boat")}")
wordResponse = input("Enter a word to make it weird: ")
print(makeItWeird(wordResponse))

# Pass


def barelyAFunction():
    pass  # no error!

# Positional Only Arguments


def argumentsInOrder(a, b, c, /):
    print(f"First {a}, then {b}, last {c}")


argumentsInOrder("first", "middle", "last")
# argumentsInOrder(a="first", b="last", c="middle")
# # ^ Error: Unexpected Keyword Argument

# Keyword Only Arguments


def argumentsByName(*, alpha, omega):
    print(f"I am the {alpha} and the {omega}")


argumentsByName(alpha="Zeta", omega="Bodega")
# argumentsByName("alfalfa", "nutella")
# # ^ Error: takes 0 positional arguments but 2 were given

# Positional-Only and Keyword-only


def argumentSoup(pos1, pos2, pos3, /, *, key1, key2, key3):
    print(f"Positionals: {pos1}, {pos2}, {pos3}")
    print(f"Keywords: {key1}, {key2}, {key3}")


argumentSoup("first pos", "second pos", "third pos",
             key3="third key", key1="first key", key2="second key")


# Recursion
def stalactite(eons):
    if eons > 0:
        for i in range(eons):
            print("#", end='')
        print()
        stalactite(eons-1)
    else:
        print(f"\n\n\n\nWhoah look up!")


stalactite(4)
# stalactite(20)
