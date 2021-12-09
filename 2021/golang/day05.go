package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct {
	x int
	y int
}

func getDelta(a int, b int) int {
	if b > a {
		return 1
	} else if b < a {
		return -1
	}
	return 0
}

func getDistance(a int, b int) int {
	distance := a - b
	if distance < 0 {
		distance *= -1
	}
	return distance + 1
}

func solveDay5(lines []string, useDiagonals bool) int {
	G := make(map[point]int)
	for _, line := range lines {
		startX, startY, endX, endY := 0, 0, 0, 0
		n, _ := fmt.Sscanf(line, "%d,%d -> %d,%d", &startX, &startY, &endX, &endY)
		_ = n

		deltaX, deltaY := getDelta(startX, endX), getDelta(startY, endY)
		var xs, ys []int

		if deltaX == 0 {
			distance := getDistance(startY, endY)
			for i := 0; i < distance; i++ {
				xs = append(xs, startX)
				ys = append(ys, deltaY*i+startY)
			}
		} else if deltaY == 0 {
			distance := getDistance(startX, endX)
			for i := 0; i < distance; i++ {
				xs = append(xs, deltaX*i+startX)
				ys = append(ys, startY)
			}
		} else if useDiagonals {
			distance := getDistance(startX, endX)
			for i := 0; i < distance; i++ {
				xs = append(xs, deltaX*i+startX)
				ys = append(ys, deltaY*i+startY)
			}
		}
		for k := range xs {
			p := point{x: xs[k], y: ys[k]}
			G[p]++
		}
	}
	sum := 0
	for _, v := range G {
		if v >= 2 {
			sum++
		}
	}
	return sum
}

func Day05() {
	file, _ := os.Open("../input/day05.input")
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	fmt.Println("Answer A:", solveDay5(lines, false))
	fmt.Println("Answer B:", solveDay5(lines, true))
}
