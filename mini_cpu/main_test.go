package main

import (
	"fmt"
	"testing"
)

func TestMiniCPU(t *testing.T) {
	cases := []struct {
		input    string
		expected []string
	}{
		{
			input: "01 00 0A 01 01 05 02 00 01 03 00 01 FF",
			expected: []string{
				"10",
				"5",
				"0",
				"0",
			},
		},
		{
			input: "01 00 03 01 01 04 04 00 01 FF",
			expected: []string{
				"12",
				"4",
				"0",
				"0",
			},
		},
		{
			input: "01 02 05 05 02 05 02 06 02 FF",
			expected: []string{
				"0",
				"0",
				"6",
				"0",
			},
		},
	}
	for _, c := range cases {
		pass := true
		result := miniCPU(c.input)

		fmt.Println("Expected:")
		for _, expected := range c.expected {
			fmt.Println(expected)
		}

		fmt.Println("Actual:")
		for _, actual := range result {
			fmt.Println(actual)
		}

		if len(result) != len(c.expected) {
			pass = false
		} else {
			for i, exp := range c.expected {
				if result[i] != exp {
					pass = false
					break
				}
			}
		}
		if pass == true {
			fmt.Println("PASS")
		} else {
			t.Errorf("FAIL")
		}
		fmt.Println("=======================")
	}
}
