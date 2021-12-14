package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func solveDay14(polymer string, rules map[string]string, iterations int) int {
	pairs := make(map[string]int)
	for i := 0; i < len(polymer)-1; i++ {
		pair := polymer[i : i+2]
		pairs[pair] += 1
	}

	for i := 0; i < iterations; i++ {
		newPairs := make(map[string]int)
		for k, v := range pairs {
			newPairs[k[0:1]+rules[k]] += v
			newPairs[rules[k]+k[1:2]] += v
		}
		pairs = newPairs
	}

	totals := make(map[string]int)
	for k, v := range pairs {
		totals[k[0:1]] += v
	}

	totals[polymer[len(polymer)-1:]] += 1
	max, min := 0, totals[polymer[len(polymer)-1:]]
	for _, v := range totals {
		if v > max {
			max = v
		} else if v < min {
			min = v
		}
	}

	return max - min
}

func Day14() {
	bytes, _ := ioutil.ReadFile("../input/day14.input")
	s := string(bytes)
	parts := strings.Split(s, "\n\n")
	polymer, rules_s := parts[0], parts[1]
	rules := make(map[string]string)

	for _, s := range strings.Split(rules_s, "\n") {
		lr := strings.Split(s, " -> ")
		rules[lr[0]] = lr[1]
	}

	fmt.Println("Answer A:", solveDay14(polymer, rules, 10))
	fmt.Println("Answer B:", solveDay14(polymer, rules, 40))
}
