package main

import (
	"bufio"
	"fmt"
	"os"
)

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var N int
	//scanner.Scan()
	//fmt.Sscan(scanner.Text(), &N)
	N = nInput() //DEBUG Input

	for i := 0; i < N; i++ {
		uniquevals := make(map[rune]struct{})
		rows := 0
		//scanner.Scan()
		//line := scanner.Text()
		line := lineInput(i) //DEBUG Input
		_ = line             // to avoid unused error

		for _, char := range line {
			uniquevals[char] = struct{}{}
		}
		for j := 0; j < len(line); j++ {
			if j == 0 {
				rows = 1
			} else {
				if rune(line[j-1]) < rune(line[j]) {
					rows++
				}
			}
			if rows > len(uniquevals) {
				rows--
				break
			}
		}
		fmt.Println(rows)
	}

	// Scanner error handling
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading input:", err)
		os.Exit(1)
	}

	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println("answer") // Write answer to stdout
}

func nInput() int {
	return 5
}

func lineInput(n int) string {
	lines := []string{
		"A",
		"CBACBACBACBACBACBA",
		"CCCCCBBBBBAAAAA",
		"BDNIDPD",
		"CODINGAME",
	}

	return lines[n]
}
