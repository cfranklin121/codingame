package main

import (
	"fmt"
	"testing"
)

func TestBattleOfHeroes(t *testing.T) {
	cases := []struct {
		input []string
	}{
		{
			input: []string{"Minotaur;20;35;10", "Unicorn;16;40;14"},
		},
		{
			input: []string{"Crusader;100;65;20", "Bone dragon;1;150;45"},
		},
		{
			input: []string{"Spartans;300;300;50", "Persians;10000;10;3"},
		},
		{
			input: []string{"Panters;1;300;50", "Writers;75;200;1"},
		},
	}

	var results []string
	for _, c := range cases {
		fmt.Println("Test Case:", c)
		fmt.Println()
		results = battleOfHeroes(c.input[0], c.input[1])
	}

	for _, line := range results {
		fmt.Println(line)
	}
	fmt.Println()
}
