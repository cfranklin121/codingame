package main

import (
	"fmt"
	"strconv"
	"strings"
)

type data struct {
	name   string
	amount int
	health int
	damage int
}

func main() {
	stack1Data := ""
	stack2Data := ""
	results := battleOfHeroes(stack1Data, stack2Data)
	fmt.Println(results)
}

func battleOfHeroes(stack1Data, stack2Data string) []string {

	stack1DataSlice := strings.Split(stack1Data, ";")
	stack2DataSlice := strings.Split(stack2Data, ";")

	amount1, _ := strconv.Atoi(stack1DataSlice[1])
	health1, _ := strconv.Atoi(stack1DataSlice[2])
	damage1, _ := strconv.Atoi(stack1DataSlice[3])

	amount2, _ := strconv.Atoi(stack2DataSlice[1])
	health2, _ := strconv.Atoi(stack2DataSlice[2])
	damage2, _ := strconv.Atoi(stack2DataSlice[3])

	stack1 := data{
		name:   stack1DataSlice[0],
		amount: amount1,
		health: health1,
		damage: damage1,
	}
	stack2 := data{
		name:   stack2DataSlice[0],
		amount: amount2,
		health: health2,
		damage: damage2,
	}

	fmt.Println(stack1)
	fmt.Println(stack2)

	//Fight
	cont := true
	i := 1
	for cont {
		fmt.Printf("Round %d\n", i)

		stack1, stack2 = fight(stack1, stack2)

		fmt.Printf("%s\n", "----------") //Mid Round Seperator

		stack2, stack1 = fight(stack2, stack1)

		fmt.Printf("%s\n", "##########") //End or Round Seperator

		i++
		if i >= 11 {
			cont = false
		}
	}

	results := make([]string, 10)
	results = append(results, stack1Data)
	results = append(results, stack2Data)
	return results
}

func fight(attackers, defenders data) (data, data) {
	defendersHealthTotal := defenders.amount * defenders.health

	damage := attackers.amount * attackers.damage
	fmt.Printf("%d %s(s) attack %d %s(s) dealing %d damage\n", attackers.amount, attackers.name, defenders.amount, defenders.name, damage)
	defendersHealthTotal -= damage

	newAmount := defendersHealthTotal / defenders.health
	if defendersHealthTotal%defenders.health != 0 {
		newAmount++
	}
	fmt.Printf("%d unit(s) perish\n", defenders.amount-newAmount)
	defenders.amount = newAmount

	return attackers, defenders
}
