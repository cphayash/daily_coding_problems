package test_tools

import "fmt"

type PrintResultParams struct {
	result		interface{}
	valueType	string
	modifier	string
}

type Option func(*PrintResultParams)

func WithValueType(valueType string) Option {
	return func(p *PrintResultParams) {
		p.valueType = valueType
	}
}

func WithModifier(modifier string) Option {
	return func(p *PrintResultParams) {
		p.modifier = modifier
	}
}

type callable func(interface{}) interface{}

func AllMatch(array []bool) bool {
	count := 0
	for _, element := range array {
		if (element) {
			count += 1
		}
	}
	return count == len(array)
}

func PrintAllMatch(array []bool) {
	fmt.Println("All match:", AllMatch(array))
}

func PrintInput(inputVal interface{}) {
	fmt.Println("Input:", inputVal)
}

func PrintResult(
	result interface{},
	options ...Option,
) {
	params := &PrintResultParams{result: result}
	for _, o := range options {
		o(params)
	}
	valueType := params.valueType
	if valueType == "" {
		valueType = "Result"
	}
	fmt.Printf("%v: %v%v\n", valueType, params.modifier, params.result)
}

func PrintExpect(result interface{}, options ...Option) {
	params := &PrintResultParams{result: result}
	for _, o := range options {
		o(params)
	}
	PrintResult(
		params.result,
		WithValueType("Expect"),
		WithModifier(params.modifier),
	)
}

func PrintIsMatch(result interface{}, expect interface{}) {
	fmt.Println("Test passed:", result == expect)
}

func PrintTestResults(testResults []bool) {
	fmt.Println("\nTest results:\n\t", testResults)
}

func PrintTestIteration(
	inputVal interface{},
	result interface{},
	expect interface{},
) {
	PrintInput(inputVal)
	PrintResult(result)
	PrintExpect(expect)
	PrintIsMatch(result, expect)
}

// # def runTest(func: function, *inputArgs: Any, expect: Any) -> bool:
// def runTest(func: Callable, testCase: Dict[Any, Any]) -> bool:
//     inputVal = testCase["input"]
//     expect = testCase["expect"]
//     result = func(inputVal)
//     printTestIteration(inputVal, result, expect)
//     return result == expect
func RunTest(function callable, testCase map[interface{}]interface{}) bool {
	inputVal := testCase["input"]
	expect := testCase["expect"]
	result := function(inputVal)
	PrintTestIteration(inputVal, result, expect)
	return result == expect
}