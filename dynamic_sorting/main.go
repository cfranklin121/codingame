package main

import (
	"slices"
	"strconv"
	"strings"
)

func main() {
}

func dynamicSorting(input []string) []string {
	start := 0
	sorting := input[0]
	types := strings.Split(input[1], ",")
	n := input[2]
	nInt, _ := strconv.Atoi(n)
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

	for i := 3; i < nInt+3; i++ {
		lines = append(lines, input[i])
	}

	//slices.Reverse(expressions)
	//slices.Reverse(types)
	i := 0
	for _, expression := range expressions {
		slices.SortFunc(lines, func(a, b string) int {
			sortDirection := expression[0]

			splitA := strings.Split(a[strings.Index(a, expression[1:]):], ",")
			splitB := strings.Split(b[strings.Index(b, expression[1:]):], ",")

			toSortA := splitA[0]
			toSortB := splitB[0]

			if types[i] == "int" {
				var intA int
				var intB int
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
					if intA < intB {
						return 1
					} else if intA > intB {
						return -1
					}
					return 0
				}
				return 0

			} else {

				if sortDirection == '+' {
					return strings.Compare(toSortA, toSortB)
				}
				if sortDirection == '-' {
					return strings.Compare(toSortB, toSortA)
				}
				return 0
			}
		})
		i++
	}

	returnVals := []string{}
	for _, val := range lines {
		id := strings.Split(val, ",")

		returnVals = append(returnVals, id[0][3:])
	}
	return returnVals
}
