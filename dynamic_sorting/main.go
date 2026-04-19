package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

func main() {
}

func dynamicSorting(input []string) []string {
	for _, line := range input {
		fmt.Println("input string:", line)
	}
	start := 0
	sorting := input[0]
	//types := strings.Split(input[1], ",")
	n := input[2]
	lines := []string{}

	expressions := []string{}
	for i, char := range sorting {
		if i != 0 {
			if char == '+' || char == '-' {
				expressions = append(expressions, sorting[start:i])
				start = i
				i++
			}
		}

	}
	expressions = append(expressions, sorting[start:])

	for i := 3; i < int(n[0]-'0')+3; i++ {
		lines = append(lines, input[i])
	}

	slices.Reverse(expressions)
	for _, expression := range expressions {
		slices.SortFunc(lines, func(a, b string) int {
			sortDirection := expression[0]
			exp := expression[1:]
			index_a := strings.Index(a, exp)
			index_b := strings.Index(b, exp)

			splitA := strings.Split(a[index_a:], ",")
			splitB := strings.Split(b[index_b:], ",")

			fmt.Println(splitA)
			fmt.Println(splitB)

			toSortA := splitA[0]
			toSortB := splitB[0]

			var intA int
			var intB int
			if exp == "age" {
				temp := strings.Split(toSortA, ":")
				intA, _ = strconv.Atoi(temp[1])

				temp = strings.Split(toSortB, ":")
				intB, _ = strconv.Atoi(temp[1])

				if sortDirection == '+' {
					if intA < intB {
						return -1
					} else if intA > intB {
						return 1
					}
					return 0
				}
				if sortDirection == '-' {
					return strings.Compare(b[index_b:], a[index_a:])
				}
				return 0

			}

			if sortDirection == '+' {
				return strings.Compare(a[index_a:], b[index_b:])
			}
			if sortDirection == '-' {
				return strings.Compare(b[index_b:], a[index_a:])
			}
			return 0
		})
	}

	returnVals := []string{}
	for _, val := range lines {
		returnVals = append(returnVals, string(val[3]))
	}
	return returnVals
}
