package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func drawSheet(G map[point]string, maxX int, maxY int) {
	for y := 0; y <= maxY; y++ {
		for x := 0; x <= maxX; x++ {
			c := G[point{x: x, y: y}]
			if c == "" {
				c = " "
			}
			fmt.Print(c)
		}
		fmt.Print("\n")
	}
}

func Day13() {
	file, _ := os.Open("../input/day13.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	G := make(map[point]string)
	var folds []string
	maxX, maxY, A := 0, 0, 0
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, "fold") {
			folds = append(folds, line)
		} else if len(line) > 1 {
			coords := strings.Split(line, ",")
			xcoord, ycoord := coords[0], coords[1]
			x, _ := strconv.Atoi(xcoord)
			y, _ := strconv.Atoi(ycoord)
			G[point{x: x, y: y}] = "#"
			if x > maxX {
				maxX = x
			}
			if y > maxY {
				maxY = y
			}
		}
	}
	for _, fold := range folds {
		parts := strings.Split(fold, "=")
		axis := string(parts[0][-1+len(parts[0])])
		n, _ := strconv.Atoi(parts[1])
		Gnew := make(map[point]string)
		for p := range G {
			if axis == "y" {
				if p.y < n {
					Gnew[p] = "#"
				} else {
					pFlip := point{x: p.x, y: p.y - 2*(p.y-n)}
					Gnew[pFlip] = "#"
				}
			} else {
				if p.x < n {
					Gnew[p] = "#"
				} else {
					pFlip := point{x: p.x - 2*(p.x-n), y: p.y}
					Gnew[pFlip] = "#"
				}
			}
		}
		if axis == "y" {
			maxY /= 2
		} else {
			maxX /= 2
		}
		G = Gnew
		if A == 0 {
			A = len(G)
		}
	}

	print("Answer A:", A)
	print("Answer B:")
	drawSheet(G, maxX, maxY)
}
