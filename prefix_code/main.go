package main

import "fmt"

func main() {
	var n int
	//fmt.Scan(&n)
	n = nInput() //Debug Input

	code := make(map[string]int)

	for i := 0; i < n; i++ {
		var b string
		var c int
		//fmt.Scan(&b, &c)
		b = bInput(i) //Debug Input
		c = cInput(i) //Debug Input
		asciiChar := string(rune(c))
		code[b] = c
		_ = asciiChar
	}
	var s string
	//fmt.Scan(&s)
	s = sInput() //Debug Input
	_ = s

	word := []string{}
	chunck := ""
	cont := true
	failIndex := 0
	remaining := len(s)

	for i, j := range s {
		if cont == false {
			break
		}
		chunck = chunck + string(j)
		for bVal, cVal := range code {
			if chunck == bVal {
				word = append(word, string(rune(cVal)))
				remaining -= len(chunck)
				chunck = ""
				cont = true
				failIndex = i + 1
				break
			}
		}
	}
	if cont == false {
		fmt.Printf("DECODE FAIL AT INDEX %d\n", failIndex)
		return
	}

	if remaining > 0 {
		fmt.Printf("DECODE FAIL AT INDEX %d\n", failIndex)
		return
	}

	for _, i := range word {
		fmt.Print(i)
	}
	fmt.Print("\n")

}

func nInput() int {
	return 5
}

func bInput(i int) string {
	b := []string{
		"1",
		"001",
		"000",
		"011",
		"010",
	}
	/*
		b := []string{
			"11",
			"1001",
			"000011",
			"000010",
			"0011",
			"011",
			"000001",
			"00101",
			"000000",
			"00100",
			"10111",
			"1000",
			"00011",
			"10110",
			"010",
			"10101",
			"00010",
			"10100",

		}*/
	return b[i]
}

func cInput(i int) int {
	c := []int{
		97,
		98,
		114,
		99,
		100,
	}
	/*
		c := []int{
			32,
			97,
			98,
			99,
			100,
			101,
			102,
			104,
			73,
			105,
			108,
			110,
			111,
			114,
			116,
			118,
			120,
			58,
		}*/
	return c[i]
}

func sInput() string {
	return "10010001011101010010001"
	//return "0000001000101011001101110010000111110100110110001001010110100111000011001000101110010101101000101011110111000001111000110000011101000101011110111000000010000110011011001111010011000100101"
}
