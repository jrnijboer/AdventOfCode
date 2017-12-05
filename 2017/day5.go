package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main() {
	var instructionsA = []int{}
	var instructionsB = []int{}
	file, _ := os.Open("day5.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		instruction, _ := strconv.Atoi(scanner.Text())
		instructionsA = append(instructionsA, instruction)
		instructionsB = append(instructionsB, instruction)
	}
	solve(instructionsA, false)
	solve(instructionsB, true)
}

func solve(instructions []int, B bool) {
	steps := 0
	pos := 0
	size := len(instructions)
	for ;; {
		if instructions[pos] >= 3 && B {
			instructions[pos]--
			pos += instructions[pos] + 1
		} else {
			instructions[pos]++
			pos += instructions[pos] - 1
		}
		steps++
		if pos > size - 1 || pos < 0 {
			fmt.Printf("it took %v steps to finish\n", steps)
			break
		}
	}
}

