package main

import (
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fmt.Println("MiniCPU")
}

func miniCPU(program string) []string {
	r := []byte{0, 0, 0, 0}
	var x byte
	var y byte
	for i := 0; i < len(program); i += 9 {
		dec, err := hex.DecodeString(program[i : i+2])
		if err != nil {
			fmt.Fprintln(os.Stderr, "err =", err)
		}
		instruction := dec[0]

		if instruction == 255 {
			if i >= len(program)-3 {
				break
			}
		}

		val1, err := hex.DecodeString(program[i+3 : i+5])
		if err != nil {
			fmt.Fprintln(os.Stderr, "err =", err)
		}
		x = val1[0]

		if instruction == 5 || instruction == 6 {
			i -= 3
		} else {
			val2, err := hex.DecodeString(program[i+6 : i+8])
			if err != nil {
				fmt.Fprintln(os.Stderr, "err =", err)
			}
			y = val2[0]
		}

		switch instruction {
		case 1: //MOV
			r[x] = y
		case 2: //ADD
			r[x] += r[y]
		case 3: //SUB
			r[x] -= r[y]
		case 4: //MUL
			r[x] *= r[y]
		case 5: //INC
			r[x] += 1
		case 6: //DEC
			r[x] -= 1
		}
	}

	// Print the final value of each register R0, R1, R2, R3, one value per line
	rInt := []int{}
	for _, bit := range r {
		rInt = append(rInt, int(bit))
	}

	rString := []string{}
	for _, bit := range rInt {
		rString = append(rString, strconv.Itoa(bit))
	}
	return rString

}
