package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func checkCorruption(chunk string) (bool, []string) {
	lookup := map[string]string{"}": "{", "]": "[", ")": "(", ">": "<"}
	S, chars := make([]string, 0), strings.Split(chunk, "")
	for _, c := range chars {
		if c == "{" || c == "[" || c == "(" || c == "<" {
			S = append(S, c)
		} else if lookup[c] == S[len(S)-1] {
			S = S[:len(S)-1]
		} else {
			return true, []string{c}
		}
	}
	return false, S
}

func Day10() {
	errorScores := map[string]int{")": 3, "]": 57, "}": 1197, ">": 25137}
	closingScores := map[string]int{"(": 1, "[": 2, "{": 3, "<": 4}
	var errors []string
	A, B := 0, make([]int, 0)
	file, _ := os.Open("../input/day10.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		err, res := checkCorruption(line)
		if err {
			errors = append(errors, res[0])
		} else {
			score := 0
			for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 { //reverse slice
				res[i], res[j] = res[j], res[i]
			}
			for _, r := range res {
				score = score*5 + closingScores[r]
			}
			B = append(B, score)
		}
	}

	for _, e := range errors {
		A += errorScores[e]
	}

	fmt.Println("Answer A:", A)
	sort.Ints(B)
	fmt.Println("Answer B:", B[len(B)/2])
}
