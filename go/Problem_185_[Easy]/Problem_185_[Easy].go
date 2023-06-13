package main
import (
	"test_tools"
)
/*
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
*/

type TestCase struct {
	input [2]map[string][2]int
	expect int
}


func buildSet(values []int) map[int]struct{} {
	set := map[int]struct{}{}
	for i := 0; i < len(values); i++ {
		value := values[i]
		set[value] = struct{}{}
	}
	return set
}

func getIntersection(
	masterSet map[int]struct{},
	set map[int]struct{},
) map[int]struct{} {
	for k := range masterSet {
		if _, contained := set[k]; !contained {
			delete(masterSet, k)
		}
	}

	return masterSet
}


func getRange(startVal int, length int) []int {
	arr := []int{}
	for i := startVal; i < startVal + length; i++ {
		arr = append(arr, i)
	}

	return arr
}


func getSizeOfIntersection(rectangles [2]map[string][2]int) int {
	masterSetX := map[int]struct{}{}
	masterSetY := map[int]struct{}{}
	for i := 0; i < len(rectangles); i++ {
		rectangle := rectangles[i]
		topLeft := rectangle["top_left"]
		dimensions := rectangle["dimensions"]

		rangeX := buildSet(getRange(topLeft[0], dimensions[0]))
		rangeY := buildSet(getRange(topLeft[1], dimensions[1]))

		if len(masterSetX) == 0 {
			masterSetX = rangeX
		} else {
			masterSetX = getIntersection(masterSetX, rangeX)
		}
		if len(masterSetY) == 0 {
			masterSetY = rangeY
		} else {
			masterSetY = getIntersection(masterSetY, rangeY)
		}
	}

	return len(masterSetX) * len(masterSetY)
}

func main() {
	testCases := []TestCase {
		{
			input: [2]map[string][2]int {
				map[string][2]int{
					"top_left": [2]int{1, 4},
					"dimensions": [2]int{3, 3}, // width, height
				},
				map[string][2]int{
					"top_left": [2]int{0, 5},
					"dimensions": [2]int{4, 3}, // width, height
				},
			},
			expect: 6,
		},
	}

	testResults := []bool{}

	for i := 0; i < len(testCases); i++ {
		testCase := testCases[i]
		inputVal := testCase.input
		expect := testCase.expect
		result := getSizeOfIntersection(inputVal)
		isMatch := result == expect
		test_tools.PrintTestIteration(inputVal, result, expect)
		testResults = append(testResults, isMatch)
		// testResults = append(testResults, RunTest(getSizeOfIntersection, testCase))
	}
	test_tools.PrintTestResults(testResults)
}