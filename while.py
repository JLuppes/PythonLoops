# While Loops
keepPlaying = True
while keepPlaying:
    response = input("Keep playing? (y/n):")
    if response.lower() in ['n', 'no']: keepPlaying = False
print("Game Over!")

# Run a Certain Amount
runTimes = 3
while runTimes > 0:
    print(f'RunTimes is now {runTimes}')
    runTimes -= 1
    # runTimes += 1  # Will run infinitely

# Entry Controlled
stuckInASpiral = False
while stuckInASpiral:
    print("Help I'm stuck in a spiral!")
    stuckInASpiral = True

# While True - Break
while True:
    response = input("Type 'please' to end loop. (please):")
    if response.lower() == "please": break
print("The End!")

# Continue
countDown = 10
while countDown > 0:
    countDown -= 1
    remainder = countDown % 2
    if remainder == 1: continue
    print(f"Even numbers only: {countDown}")

# Else
magicNumber = 3
# magicNumber = 300 # Number not found
countDown = 10
while countDown >= 0:
    countDown -= 1
    print(f"Countdown: {countDown}")
    if countDown == magicNumber:
        print(f"Found the magic number: {countDown}")
        break
else: 
    print("Magic number not found!")
    