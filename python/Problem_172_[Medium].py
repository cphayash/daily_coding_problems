from typing import List

"""
This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every
word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there
are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""


def startingIndices(s, words) -> List[int]:
    results = []

    if not words:
        return results
    
    wordsSet = set(words)

    wordLen = len(words[0])

    prevWord = None
    i = 0
    while i < len(s):
        cur = s[i:i+wordLen]
        if cur in wordsSet:
            if not prevWord:
                results.append(i)
            prevWord = cur
            i += wordLen - 1
        if cur not in wordsSet:
            prevWord = None
        i += 1

    return results


tests = [
    {
        "s": "dogcatcatcodecatdog",
        "words": ["cat", "dog"],
        "expect": [0, 13],
    },
    {
        "s": "bookcarttookbookklookhookfoolcartbooktank",
        "words": ["book", "cart"],
        "expect": [0, 12, 29],
    }
]


testResults = []
for item in tests:
    s = item["s"]
    words = item["words"]
    expect = item["expect"]
    result = startingIndices(s, words)
    match = result == expect
    print(result, match)
    testResults.append(match)

print(testResults)