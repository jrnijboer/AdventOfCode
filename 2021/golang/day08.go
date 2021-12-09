package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func countOverlaps(s string, sub string) int {
	overlaps, chars := 0, strings.Split(sub, "")
	for _, c := range chars {
		if strings.Contains(s, c) {
			overlaps++
		}
	}
	return overlaps
}

func sortAlphabetic(s string) string {
	tmp := strings.Split(s, "")
	sort.Strings(tmp)
	return strings.Join(tmp, "")
}

func Day08() {
	file, _ := os.Open("../input/day08.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	A, B := 0, 0
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), " | ")
		patterns, outputs := strings.Split(parts[0], " "), strings.Split(parts[1], " ")
		var twothreefive, zerosixnine []string
		segments, wires := make(map[int]string), make(map[string]int)

		for _, pattern := range patterns {
			switch len(pattern) {
			case 2:
				segments[1] = sortAlphabetic(pattern)
			case 3:
				segments[7] = sortAlphabetic(pattern)
			case 4:
				segments[4] = sortAlphabetic(pattern)
			case 7:
				segments[8] = sortAlphabetic(pattern)
			case 5:
				twothreefive = append(twothreefive, sortAlphabetic(pattern))
			case 6:
				zerosixnine = append(zerosixnine, sortAlphabetic(pattern))
			}
		}

		for _, s := range zerosixnine {
			if countOverlaps(s, segments[1]) != 2 {
				segments[6] = s
			} else if countOverlaps(s, segments[4]) == 4 {
				segments[9] = s
			} else {
				segments[0] = s
			}
		}

		for _, s := range twothreefive {
			if countOverlaps(s, segments[1]) == 2 {
				segments[3] = s
			} else if countOverlaps(s, segments[4]) == 3 {
				segments[5] = s
			} else {
				segments[2] = s
			}
		}

		for k, v := range segments {
			wires[v] = k
		}

		factor := 1000
		for _, output := range outputs {
			if len(output) == 2 || len(output) == 3 || len(output) == 4 || len(output) == 7 {
				A++
			}
			B += factor * wires[sortAlphabetic(output)]
			factor /= 10
		}
	}
	fmt.Println("Answer A:", A)
	fmt.Println("Answer B:", B)
}
