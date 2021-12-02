package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Day02() {
	file, _ := os.Open("../input/day02.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	x, y1, y2, aim := 0, 0, 0, 0

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		value, _ := strconv.Atoi(fields[1])
		switch fields[0] {
		case "forward":
			x += value
			y2 += value * aim
		case "up":
			y1 -= value
			aim -= value
		case "down":
			y1 += value
			aim += value
		}
	}

	fmt.Println("Answer A:", x*y1)
	fmt.Println("Answer A:", x*y2)
}
