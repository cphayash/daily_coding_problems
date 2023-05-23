import sys

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups
of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people
in the building. Return it as a pair of (start, end) timestamps. You can assume
the building always starts off and ends up empty, i.e. with 0 people inside.
"""

"""
Plan

I'm thinking that we can just store the count of people in the building at a given
timestamp.  Each timestamp will be the "start" of the count, meaning the count
of people in the building is X, starting at Y.

This simplifies the problem to mean "the word 'enter' means add, the word 'exit'
means subtract.

This makes it simple to, once we have our full data set, look for the timestamp
with the highest count, and then look to the next timestamp to get the end time,
giving us the time range.  That actually might be overkill, since we don't have
instructions more specific.
"""

# Time: O(n) | n is num entries in actions list
# Space: O(1)
def getPeopleCount(actions) -> int:
    actionHandler = {
        "exit": -1,
        "enter": 1,
    }

    runningCount = 0
    maxCountTime = [0, runningCount] # [timestamp, count]
    for actionDict in actions:
        moveType = actionDict["type"]
        runningCount += actionHandler[moveType] * actionDict["count"]
        timestamp = actionDict["timestamp"]
        if runningCount > maxCountTime[1]:
            maxCountTime = [timestamp, runningCount]

    return maxCountTime[0]


actions = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"}, # 3
    {"timestamp": 1526589928, "count": 2, "type": "exit"},  # 1
    {"timestamp": 1526689928, "count": 5, "type": "enter"}, # 6
    {"timestamp": 1526889928, "count": 1, "type": "enter"}, # 7
    {"timestamp": 1527589928, "count": 2, "type": "enter"}, # 9
    {"timestamp": 1527590028, "count": 6, "type": "exit"},  # 3
    {"timestamp": 1530000028, "count": 1, "type": "exit"},  # 2
    {"timestamp": 1530050028, "count": 1, "type": "exit"},  # 1
    {"timestamp": 1530150028, "count": 1, "type": "exit"},  # 0
]


maxPeople = getPeopleCount(actions)

print(maxPeople)