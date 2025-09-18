# Collections
# List, Set, Dictionary, Tuple

## List
birdList = ['eagle', 'hawk', 'chickadee']
print(birdList)

### Access a List
### Lists are ordered and changeable, duplicates allowed
print(birdList[0]) # eagle
birdList[0] = "ostrich"
print(birdList[0]) # ostrich

### Duplicates are allowed
birdList[1] = "ostrich"
print(birdList) # ['ostrich', 'ostrich', 'chickadee']

### Check length with len()
print(f"Length of birdList: {len(birdList)}") # 3

## Tuple
### Ordered, unchangeable, duplicates allowed
lunchTuple = ("Pizza", "Salad", "Cookie")
print(lunchTuple)
print(lunchTuple[1])

## Dictionary
### Key-Value Pairs, ordered, changable, no duplicates
bestPets = {
    "dog": "Guts",
    "cat": "Ducky",
    "gremlin": "Ace"    
}
print(f"Best dog: {bestPets["dog"]}")
print(f"Best cat: {bestPets["cat"]}")
print(f"Best gremlin: {bestPets["gremlin"]}")

### Length (number of items)
print(f"Number of best pets: {len(bestPets)}")

## Set
### Unordered, unchangeable, unindexed
funWords = {"skedaddle", "florf", "shazow"}
print(f"Some Fun words: {funWords}")
for thisWord in funWords:
    print(f"Look at this word: {thisWord}")
