/*
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form
racecar, which is a palindrome. daily should return false, since there's no
rearrangement that can form a palindrome.
*/

function couldBePalindrome(str) {
    let charCounts = {};

    for (let char of str) {
        if (!charCounts.hasOwnProperty(char)) {
            charCounts[char] = 0;
        }
        charCounts[char]++;
    }

    // let charCountsEqOne = 0;

    // for (const [_, count] of Object.entries(charCounts)) {
    //     if (count === 1) {
    //         charCountsEqOne++;
    //     }
    // }

    const charCountsEqOne = Object.values(charCounts).reduce(function(accumulator, count) {
        if (count === 1) {
            return accumulator + count;
        }
        return 0;
    });

    return charCountsEqOne < 2;
}


testCases = [
    {
        input: "carrace",
        expect: true,
    },
    {
        input: "carraces",
        expect: false,
    },
];


testResults = [];
testCases.forEach(testCase => {
    const input = testCase.input;
    const result = couldBePalindrome(input);
    const expect = testCase.expect;
    const isMatch = result === expect;
    console.log(`Input: ${input}`);
    console.log(`Result: ${result}`);
    console.log(`Expect: ${expect}`);
    console.log(`Test passed: ${isMatch}\n`);
    testResults.push(isMatch);
});
console.log(`Test Results:\n\t${testResults}`);