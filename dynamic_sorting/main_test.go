package main

import (
	"fmt"
	"testing"
)

func TestDynamicSorting(t *testing.T) {
	cases := []struct {
		input    []string
		expected []string
	}{
		{
			input: []string{
				"+name",
				"string",
				"3",
				"id:1,name:maria",
				"id:2,name:jason",
				"id:3,name:robert",
			},
			expected: []string{
				"2",
				"1",
				"3",
			},
		},
		{
			input: []string{
				"+age-name",
				"int,string",
				"6",
				"id:1,name:hugo,age:1",
				"id:2,name:maria,age:12",
				"id:3,name:jason,age:2",
				"id:4,name:amit,age:15",
				"id:5,name:maria,age:6",
				"id:6,name:robert,age:12",
			},
			expected: []string{
				"1",
				"3",
				"5",
				"6",
				"2",
				"4",
			},
		},
	}

	var pass bool
	for i, c := range cases {
		fmt.Println("Case", i+1)
		result := dynamicSorting(c.input)

		if len(result) != len(c.expected) {
			fmt.Printf("Expected: %s\n", c.expected)
			fmt.Printf("Actual  : %s\n", result)
			fmt.Println("FAIL")
			pass = false
			continue
		}

		match := true
		for j, r := range result {
			if r != c.expected[j] {
				match = false
				pass = false
			}
		}

		if match {
			fmt.Printf("Expected: %s\n", c.expected)
			fmt.Printf("Actual  : %s\n", result)
			fmt.Println("PASS")
			pass = true
		} else {
			fmt.Printf("Expected: %s\n", c.expected)
			fmt.Printf("Actual  : %s\n", result)
			fmt.Println("FAIL")
			pass = false
		}

	}
	if pass {
		fmt.Println("=====PASS=====")
	} else {
		t.Errorf("=====FAIL=====\n")
	}
}
