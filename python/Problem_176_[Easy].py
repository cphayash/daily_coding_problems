from collections import Counter
"""
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1
to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map
a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

"""
I think what we can do here is simply use a Counter to get character counts
for all characters.  Then, we can just look at the sorted count values for each
and see if they sorted lists are equal because we don't actually care what the
mappings are, we just care that they're possible.
"""

# Time: O(nlogn) | n is num chars in max(s1, s2)
# Space: O(n) | n is num chars in max(s1, s2)
def checkMapping(s1: str, s2: str) -> bool:
    return sorted(Counter(s1).values()) == sorted(Counter(s2).values())


testCases = [
    {
        "input": ("abc", "bcd"),
        "expect": True,
    },
    {
        "input": ("foo", "bar"),
        "expect": False,
    }
]


"""
Test the solution
"""
testResults = []

for testCase in testCases:
    s1, s2 = testCase["input"]
    expect = testCase["expect"]
    res = checkMapping(s1, s2)
    match = res == expect
    print(f"res: {res}, expect: {expect}")
    print(match)
    testResults.append(match)
print(testResults)