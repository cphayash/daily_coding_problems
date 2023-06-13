from random import randint
"""
This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are
computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed
by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five
followed by a five.

Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.
"""

def xFollowedByY(val1: int, val2: int) -> int:
    val1Found = False
    val2Found = False
    count = 0

    while not (val1Found and val2Found):
        randomNum = randint(1, 6)
        val2Found = val1Found and randomNum == val2
        val1Found = val1Found or randomNum == val1
        count += 1

    return count



testRunCount = 10
testResults = [0, 0]
# Run 5 times
for _ in range(testRunCount):
    fiveSix = xFollowedByY(5, 6)
    fiveFive = xFollowedByY(5, 5)
    if fiveSix < fiveFive:
        testResults[0] += 1
    else:
        testResults[1] += 1
    print()
    print(f"5 followed by 6: {fiveSix}")
    print(f"5 followed by 5: {fiveFive}")

print()
print(f"fiveSix wins: {testResults[0]} ({testResults[0]/testRunCount*100}%)")
print(f"fiveFive wins: {testResults[1]} ({testResults[1]/testRunCount*100}%)")