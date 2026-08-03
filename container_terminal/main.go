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
		topOfStack := []byte{}
		uniqueVals := make(map[rune]struct{})
		rows := 0
		//scanner.Scan()
		//line := scanner.Text()
		line := lineInput(i) //DEBUG Input

		for _, char := range line { //Find unique characters
			uniqueVals[char] = struct{}{}
		}

		var largestIndex int
		for j := 0; j < len(line); j++ {
			if j == 0 {
				rows = 1
				topOfStack = append(topOfStack, line[j])
				largestIndex = len(topOfStack) - 1
			} else if line[j] < line[j-1] {
				if line[j] > topOfStack[largestIndex] {
					topOfStack = append(topOfStack, line[j])
					largestIndex = len(topOfStack) - 1
				} else {
					var diff byte
					smallestDif := byte(27)
					smallestIndex := 0
					for k := range topOfStack {
						diff = topOfStack[largestIndex] - topOfStack[k]
						if diff < smallestDif {
							smallestDif = diff
							smallestIndex = k
						}
					}
					topOfStack[smallestIndex] = line[j]
				}

			} else if line[j] > line[j-1] {
				rows++
				topOfStack = append(topOfStack, line[j])
			}
			if rows > len(uniqueVals) {
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
	return 1
}

func lineInput(n int) string {
	lines := []string{
		//"A",
		//"CBACBACBACBACBACBA",
		//"CCCCCBBBBBAAAAA",
		//"BDNIDPD",
		"CODINGAME",
	}

	return lines[n]
}
