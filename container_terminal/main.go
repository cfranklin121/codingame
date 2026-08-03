package main

import (
	"bufio"
	"fmt"
	"os"
)

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
			if j == 0 { //-----------------------------------------------First Container
				rows = 1
				topOfStack = append(topOfStack, line[j])
				largestIndex = len(topOfStack) - 1
			} else if line[j] < topOfStack[largestIndex] { //------------Larger Container
				var diff int
				smallestDif := 27
				smallestIndex := 0
				for k := range topOfStack {
					diff = int(topOfStack[k]) - int(line[j])
					if diff < smallestDif && diff >= 0 {
						smallestDif = diff
						smallestIndex = k
					}
				}
				topOfStack[smallestIndex] = line[j]
			} else if line[j] > topOfStack[largestIndex] { //---------------Smaller Container
				rows++
				topOfStack = append(topOfStack, line[j])
				largestIndex = len(topOfStack) - 1
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

}

func nInput() int {
	return 15
}

func lineInput(n int) string {
	lines := []string{
		"C",
		"JS",
		"VB",
		"CPP",
		"PHP",
		"JAVA",
		"PERL",
		"RUBY",
		"MYSQL",
		"PYTHON",
		"GROOVY",
		"PASCAL",
		"POSTGRES",
		"HIBERNATE",
		"KUBERNETES",
	}

	return lines[n]
}
