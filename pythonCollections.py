# Collections
# List, Set, Dictionary, Tuple

## List
### Lists are ordered and changeable, duplicates allowed
birdList = ['eagle', 'hawk', 'chickadee']
print(birdList) # ['eagle', 'hawk', 'chickadee']

### Access a List
print(birdList[0]) # eagle
birdList[0] = "ostrich"
print(birdList[0]) # ostrich

### Duplicates are allowed
birdList[1] = "ostrich"
print(birdList) # ['ostrich', 'ostrich', 'chickadee']
print(birdList.count("ostrich")) # 2

### Check length with len()
print(f"Length of birdList: {len(birdList)}") # 3

### Add New Items
birdList.append("grackle")
print(birdList) # ['ostrich', 'ostrich', 'chickadee', 'grackle']

### Remove a Specific Item
birdList.remove("chickadee")
print(birdList) # ['ostrich', 'ostrich', 'grackle']

### Remove and return the last item
print(f"I just caught a {birdList.pop()}!") # I just caught a grackle!
print(birdList) # ['ostrich', 'ostrich']

## Tuple
### Ordered, unchangeable, duplicates allowed
lunchTuple = ("Pizza", "Salad", "Cookie")
print(lunchTuple) # ('Pizza', 'Salad', 'Cookie')
print(lunchTuple[1]) # Salad

## Dictionary
### Key-Value Pairs, ordered, changable, no duplicates
bestPets = {
    "dog": "Guts",
    "cat": "Ducky",
    "gremlin": "Ace"    
}
print(f"Best dog: {bestPets["dog"]}") # Best dog: Guts
print(f"Best cat: {bestPets["cat"]}") # Best cat: Ducky 
print(f"Best gremlin: {bestPets["gremlin"]}") # Best gremlin: Ace

### Length (number of items)
print(f"Number of best pets: {len(bestPets)}") # 3

## Set
### Unordered, unchangeable, unindexed
funWords = {"skedaddle", "florf", "shazow"}
print(f"Some Fun words: {funWords}") # Some Fun words: {'florf', 'skedaddle', 'shazow'}
for thisWord in funWords:
    print(f"Look at this word: {thisWord}") # Look at this word: florf ...
    
funWords.add("squiggly")
print(funWords) # {'squiggly', 'florf', 'skedaddle', 'shazow'}
funWords.remove("florf")
print(funWords) # {'squiggly', 'skedaddle', 'shazow'}
