package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func flashOctopus(G map[point]int, p point, C int, R int) {
	if C != R {
		defer fmt.Println("assert error, C != R")
		os.Exit(1)
	}
	DX := []int{-1, 0, 1}
	DY := []int{-1, 0, 1}
	G[p] = -1
	for _, dx := range DX {
		for _, dy := range DY {
			nextP := point{x: p.x + dx, y: p.y + dy}
			if p.x+dx >= 0 && p.x+dx < C && p.y+dy >= 0 && p.y+dy < R && G[nextP] != -1 {
				G[nextP]++
				if G[nextP] > 9 {
					flashOctopus(G, nextP, C, R)
				}
			}
		}
	}
}

func Day11() {
	file, _ := os.Open("../input/day11.input")
	defer file.Close()
	G := make(map[point]int)
	scanner := bufio.NewScanner(file)
	R, C, steps, totalFlashes := 0, 0, 0, 0

	for scanner.Scan() {
		line := scanner.Text()
		R++
		C = len(line)
		for x, c := range strings.Split(line, "") {
			n, _ := strconv.Atoi(c)
			G[point{x: x, y: R - 1}] = n
		}
	}

	for {
		for k := range G {
			G[k]++
		}

		for k, v := range G {
			if v > 9 {
				flashOctopus(G, k, R, C)
			}
		}

		lights := 0
		for k, v := range G {
			if v == -1 {
				G[k] = 0
				lights++
			}
		}

		steps++
		if len(G) == lights {
			fmt.Println("Answer B:", steps)
			break
		}
		totalFlashes += lights
		if steps == 100 {
			fmt.Println("Answer A:", totalFlashes)
		}
	}
}
