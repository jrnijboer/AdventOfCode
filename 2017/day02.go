package main

import (
	"fmt"
	"strconv"
	"bufio"
	"os"
	"strings"
)

func main() {
	checksumA := 0
	checksumB := 0
	file, _ := os.Open("day02.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		numbers := getNumbersFromLine(scanner.Text())
		checksumA += calculateChecksumA(numbers[:])
		checksumB += calculateChecksumB(numbers[:])
	}
	fmt.Printf("Checksum for part A is %v\n", checksumA)
	fmt.Printf("Checksum for part B is %v\n", checksumB)
}

func getNumbersFromLine(input string) []int {
	arr := strings.Split(input, "\t")
	var numbers = []int{}
	for _, i := range arr {
		n, _ := strconv.Atoi(i)
		numbers = append(numbers,n)
	}
	return numbers
}

func calculateChecksumB(numbers []int) int {
	for i := 0; i < len(numbers); i++ {
		for j := 0; j < len(numbers); j++ {
			if numbers[i] %  numbers[j] == 0 && i != j {
				return numbers[i] / numbers[j]
			}
		}
	}
	panic("no checksum found")
}

func calculateChecksumA(numbers []int) int {
	min := 20000000
	max := 0
	for i := 0; i < len(numbers); i++ {
		if numbers[i] > max {
			max = numbers[i]
		}
		if numbers[i] < min {
			min = numbers[i]

		}
	}
	return max - min
}
