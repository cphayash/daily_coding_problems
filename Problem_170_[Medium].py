from typing import List, Optional, Set
"""
This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the
shortest transformation sequence from start to end such that only one letter is
changed at each step of the sequence, and each transformed word exists in the
dictionary. If there is no possible transformation, return null. Each word in
the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat",
and dictionary = {"dot", "dop", "dat", "cat"},
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat",
and dictionary = {"dot", "tod", "dat", "dar"},
return null as there is no possible transformation from dog to cat.
"""

"""
For this, what may be the most straight-forward option is to generate all of the
changes between start and end.

On the other hand, we could pop a word at a time and check if it:
    - Contains 1 change compared to the most recent word
    - Contains a change in common with end

It'll likely use a while loop to check for word options in dictionary and also
that start != end

Another option is to take one character from end and replace the corresponding
char in start with it, and check if it's in dictionary.  Do that for each idx
that has not been replaced.  Continue until termination condition.
This will result in a n^2 solution, though.  No better or worse than the other
options.
"""

# Time: O(n^2) | n is len(start)
# Space: O(n) | n is len(start)
def shortestTransform(
        start: str,
        end: str,
        dictionary: Set[str],
) -> Optional[List[str]]:
    cur = start
    tried = set()
    transform = [cur]
    while cur != end and dictionary:
        foundMatch = False
        for i in range(len(cur)):
            if i in tried:
                continue
            toTry = end[i]
            tmp = cur[:i] + toTry + cur[i+1:]
            if tmp in dictionary:
                dictionary.remove(tmp)
                cur = tmp
                transform.append(cur)
                foundMatch = True
                if cur == end:
                    return transform
            if not dictionary:
                break
        if not foundMatch:
            return None
    return transform if cur == end else None



testCases = [
    {
        "input": {
            "start": "dog",
            "end": "cat",
            "dictionary": {"dot", "dop", "dat", "cat"},
        },
        "expect": ["dog", "dot", "dat", "cat"],
    },
    {
        "input": {
            "start": "dog",
            "end": "cat",
            "dictionary": {"dot", "tod", "dat", "dar"},
        },
        "expect": None,
    },
]

testResults = []

for testCase in testCases:
    inputs = testCase["input"]
    start = inputs["start"]
    end = inputs["end"]
    dictionary = inputs["dictionary"]
    expect = testCase["expect"]
    res = shortestTransform(start, end, dictionary)
    match = res == expect
    print(f"result: {res}")
    print(f"expect: {expect}")
    print(match)
    testResults.append(match)

print(testResults)
print(f"All succeeded: {sum([1 if item else 0 for item in testResults]) == len(testResults)}")