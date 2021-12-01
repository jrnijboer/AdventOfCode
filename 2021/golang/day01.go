package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func Day01() {
	file, _ := os.Open("../input/day01.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var digits []int

	for scanner.Scan() {
		digit, _ := strconv.Atoi(scanner.Text())
		digits = append(digits, digit)
	}

	partA := 0
	for i := 1; i < len(digits); i++ {
		if digits[i] > digits[i-1] {
			partA++
		}
	}

	partB := 0
	for i := 3; i < len(digits); i++ {
		if digits[i] > digits[i-3] {
			partB++
		}
	}

	fmt.Println("Answer A:", partA)
	fmt.Println("Answer B:", partB)
}
