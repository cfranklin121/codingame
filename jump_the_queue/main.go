package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)
	var inputs []string

	var g, e int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &g, &e)

	groups := []string{}
	for i := 0; i < g; i++ {
		scanner.Scan()
		group := scanner.Text()
		groups = append(groups, group)
	}

	que := []int64{}

	scanner.Scan()
	inputs = strings.Split(scanner.Text(), " ")
	for i := 0; i < e; i++ {
		event, _ := strconv.ParseInt(inputs[i], 10, 32)
		if event > 0 {
			result := inGroup(event, groups)
			if result >= 0 { // Friend is in group
				friendPos := FriendsInQue(que, groups[result])
				if friendPos >= 0 { //Friend in line
					que = insertToQue(que, friendPos, event)
				} else {
					que = append(que, event)
				}

			} else {
				que = append(que, event)
			}
		} else {
			fmt.Println(que[0])
			que = que[1:]
		}
	}

}

func inGroup(event int64, groups []string) int {
	for j := 0; j < len(groups); j++ {
		groupInt := strings.Split(groups[j], " ")

		for k := 0; k < len(groupInt); k++ {
			studentID, _ := strconv.ParseInt(groupInt[k], 10, 32)
			if event == studentID {
				return j
			}
		}
	}

	return -1
}

func FriendsInQue(que []int64, group string) int {
	pos := -1
	for i := 0; i < len(que); i++ {
		groupInt := strings.Split(group, " ")
		for j := 0; j < len(groupInt); j++ {
			studentID, _ := strconv.ParseInt(groupInt[j], 10, 32)
			if studentID == que[i] {
				pos = i
			}
		}
	}
	return pos
}

func insertToQue(que []int64, friendPos int, friend int64) []int64 {
	front := que[:friendPos + 1]
	back := que[friendPos + 1:]

	newQue := []int64{}
	newQue = append(newQue, front...)
	newQue = append(newQue, friend)
	newQue = append(newQue, back...)

	return newQue
}
