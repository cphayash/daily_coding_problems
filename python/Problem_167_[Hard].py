from typing import List, Tuple


"""
This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the
concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"],
    return [(0, 1), (1, 0), (2, 3)].
"""

RETURN_TYPE = List[Tuple[int]]


# Time: O(n^2) | n is len(strings)
# Space: O(n) | worst case would be 3n, which evaluates to n
def findPalindromes(strings) -> RETURN_TYPE:
    results = []
    reversedStrings = [string[::-1] for string in strings]

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            concat1 = strings[i] + strings[j]
            concat2 = reversedStrings[j] + reversedStrings[i]
            concat3 = strings[j] + strings[i]
            concat4 = reversedStrings[i] + reversedStrings[j]
            if concat1 == concat2:
                results.append((i, j))
            if concat3 == concat4:
                results.append((j, i))
    return results


def testFunc(func, tests) -> RETURN_TYPE:
    testResults = []
    for test in tests:
        testData = test[0]
        expectedRes = test[1]
        testRes = func(testData)
        print(testRes)
        print(expectedRes)
        match = testRes == expectedRes
        print(match)
        testResults.append(match)
    
    return testResults


tests = [
    (
        ["code", "edoc", "da", "d"],
        [(0, 1), (1, 0), (2, 3)],
    ),
    (
        ["abc", "cba", "ba", "xyz"],
        [(0, 1), (1, 0), (0, 2)],
    ),
    (
        ["race", "car", "rac"],
        [(0, 1), (1, 2), (2, 1)],
    ),
]


testRes = testFunc(findPalindromes, tests)
successfulTest = True
for test in testRes:
    successfulTest = successfulTest and test
print(f"Success: {successfulTest}")