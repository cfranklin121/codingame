package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)
	var inputs []string

	var g, e int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &g, &e)

	for i := 0; i < g; i++ {
		scanner.Scan()
		group := scanner.Text()
		_ = group // to avoid unused error
	}
	scanner.Scan()
	inputs = strings.Split(scanner.Text(), " ")
	for i := 0; i < e; i++ {
		event, _ := strconv.ParseInt(inputs[i], 10, 32)
		_ = event
	}

	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println("answer") // Write answer to stdout
}
