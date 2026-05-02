package main

import (
	"fmt"
	"testing"
)

func TestDynamicSorting(t *testing.T) {
	cases := []struct {
		input    []string
		expected []string
	}{
		{
			input: []string{
				"+name",
				"string",
				"3",
				"id:1,name:maria",
				"id:2,name:jason",
				"id:3,name:robert",
			},
			expected: []string{
				"2",
				"1",
				"3",
			},
		},
		{
			input: []string{
				"+age-name",
				"int,string",
				"6",
				"id:1,name:hugo,age:1",
				"id:2,name:maria,age:12",
				"id:3,name:jason,age:2",
				"id:4,name:amit,age:15",
				"id:5,name:maria,age:6",
				"id:6,name:robert,age:12",
			},
			expected: []string{
				"1",
				"3",
				"5",
				"6",
				"2",
				"4",
			},
		},
		{
			input: []string{
				"+age+name",
				"int,string",
				"33",
				"id:1,name:hugo,age:10",
				"id:2,name:maria,age:2",
				"id:3,name:jason,age:15",
				"id:4,name:amit,age:8",
				"id:5,name:maria,age:5",
				"id:6,name:david,age:20",
				"id:7,name:theo,age:22",
				"id:8,name:fabien,age:13",
				"id:9,name:michael,age:100",
				"id:10,name:jordan,age:21",
				"id:11,name:jean,age:7",
				"id:12,name:yoan,age:19",
				"id:13,name:marie,age:8",
				"id:14,name:justin,age:19",
				"id:15,name:aria,age:21",
				"id:16,name:stark,age:2",
				"id:17,name:julia,age:18",
				"id:18,name:eva,age:18",
				"id:19,name:angelina,age:8",
				"id:20,name:tori,age:22",
				"id:21,name:ariana,age:21",
				"id:22,name:sasha,age:2",
				"id:23,name:caprice,age:2",
				"id:24,name:clara,age:18",
				"id:25,name:maurice,age:15",
				"id:26,name:johny,age:17",
				"id:27,name:brigitte,age:51",
				"id:28,name:sophie,age:22",
				"id:29,name:sophia,age:21",
				"id:30,name:aurore,age:22",
				"id:31,name:david,age:9",
				"id:32,name:damien,age:19",
				"id:33,name:jason,age:19",
			},
			expected: []string{
				"23",
				"2",
				"22",
				"16",
				"5",
				"11",
				"4",
				"19",
				"13",
				"31",
				"1",
				"8",
				"3",
				"25",
				"26",
				"24",
				"18",
				"17",
				"32",
				"33",
				"14",
				"12",
				"6",
				"15",
				"21",
				"10",
				"29",
				"30",
				"28",
				"7",
				"20",
				"27",
				"9",
			},
		},
		{
			input: []string{
				"+age-name+size",
				"int,string,int",
				"62",
				"id:1,name:hugo,age:10,size:165",
				"id:2,name:maria,age:12,size:85",
				"id:3,name:jason,age:15,size:190",
				"id:4,name:amit,age:18,size:60",
				"id:5,name:maria,age:15,size:155",
				"id:6,name:david,age:20,size:160",
				"id:7,name:theo,age:22,size:190",
				"id:8,name:fabien,age:13,size:180",
				"id:9,name:michael,age:15,size:80",
				"id:10,name:jordan,age:21,size:185",
				"id:11,name:jean,age:17,size:190",
				"id:12,name:yoan,age:19,size:165",
				"id:13,name:marie,age:18,size:170",
				"id:14,name:justin,age:19,size:170",
				"id:15,name:aria,age:21,size:170",
				"id:16,name:stark,age:20,size:185",
				"id:17,name:julia,age:18,size:175",
				"id:18,name:eva,age:18,size:185",
				"id:19,name:angelina,age:18,size:65",
				"id:20,name:tori,age:22,size:155",
				"id:21,name:ariana,age:21,size:160",
				"id:22,name:sasha,age:20,size:160",
				"id:23,name:caprice,age:22,size:180",
				"id:24,name:clara,age:18,size:185",
				"id:25,name:maurice,age:15,size:190",
				"id:26,name:johny,age:17,size:195",
				"id:27,name:brigitte,age:18,size:175",
				"id:28,name:eva,age:18,size:170",
				"id:29,name:sophia,age:21,size:80",
				"id:30,name:aurore,age:22,size:190",
				"id:31,name:david,age:19,size:195",
				"id:32,name:damien,age:19,size:185",
				"id:33,name:jason,age:17,size:180",
				"id:34,name:malena,age:24,size:170",
				"id:35,name:morgan,age:75,size:75",
				"id:36,name:alina,age:15,size:160",
				"id:37,name:pierre,age:18,size:190",
				"id:38,name:yan,age:22,size:180",
				"id:39,name:ryan,age:23,size:165",
				"id:40,name:thomas,age:22,size:185",
				"id:41,name:alain,age:15,size:175",
				"id:42,name:ariana,age:21,size:165",
				"id:43,name:ayana,age:20,size:170",
				"id:44,name:arwen,age:20,size:175",
				"id:45,name:daniel,age:17,size:190",
				"id:46,name:joseph,age:18,size:180",
				"id:47,name:charlie,age:19,size:180",
				"id:48,name:ariel,age:24,size:190",
				"id:49,name:georges,age:18,size:170",
				"id:50,name:ariana,age:21,size:175",
				"id:51,name:leonard,age:26,size:165",
				"id:52,name:melissa,age:22,size:180",
				"id:53,name:amine,age:17,size:170",
				"id:54,name:coraline,age:18,size:65",
				"id:55,name:erika,age:15,size:175",
				"id:56,name:eva,age:18,size:185",
				"id:57,name:clara,age:20,size:160",
				"id:58,name:clara,age:20,size:175",
				"id:59,name:melissa,age:21,size:165",
				"id:60,name:mathieu,age:15,size:65",
				"id:61,name:alain,age:15,size:190",
				"id:62,name:morgan,age:17,size:180",
			},
			expected: []string{
				"1",
				"2",
				"8",
				"9",
				"25",
				"60",
				"5",
				"3",
				"55",
				"36",
				"41",
				"61",
				"62",
				"26",
				"11",
				"33",
				"45",
				"53",
				"37",
				"13",
				"17",
				"46",
				"49",
				"28",
				"18",
				"56",
				"54",
				"24",
				"27",
				"19",
				"4",
				"12",
				"14",
				"31",
				"32",
				"47",
				"16",
				"22",
				"6",
				"57",
				"58",
				"43",
				"44",
				"29",
				"59",
				"10",
				"21",
				"42",
				"50",
				"15",
				"38",
				"20",
				"40",
				"7",
				"52",
				"23",
				"30",
				"39",
				"34",
				"48",
				"51",
				"35",
			},
		},
	}

	var pass bool
	for i, c := range cases {
		fmt.Println("Case", i+1)
		result := dynamicSorting(c.input)

		if len(result) != len(c.expected) {
			fmt.Printf("Expected: %s\n", c.expected)
			fmt.Printf("Actual  : %s\n", result)
			fmt.Println("====FAIL====")
			pass = false
			continue
		}

		match := true
		for j, r := range result {
			if r != c.expected[j] {
				match = false
				pass = false
			}
		}

		if match {
			fmt.Printf("Expected: %s\n", c.expected)
			fmt.Printf("Actual  : %s\n", result)
			fmt.Println("====PASS====")
			pass = true
		} else {
			fmt.Printf("Expected: %s\n", c.expected)
			fmt.Printf("Actual  : %s\n", result)
			fmt.Println("====FAIL====")
			pass = false
		}

	}
	if pass {
		fmt.Println("=====PASS=====")
	} else {
		t.Errorf("=====FAIL=====\n")
	}
}
