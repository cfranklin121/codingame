package main

import (
	"fmt"
	"testing"
)

func TestBattleOfHeroes(t *testing.T) {
	cases := []struct {
		input    []string
		expected bool
	}{
		{
			input:    []string{"Minotaur;20;35;10", "Unicorn;16;40;14"},
			expected: false,
		},
	}

	var results []string
	for _, c := range cases {
		results = battleOfHeroes(c.input[0], c.input[1])
	}

	for _, line := range results {
		fmt.Println(line)
	}

}
