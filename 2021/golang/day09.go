package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func Day09() {
	file, _ := os.Open("../input/day09.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	G, lows := make(map[point]int), make([]point, 0)
	R, C, A := 0, 0, 0
	dx, dy := [4]int{1, 0, -1, 0}, [4]int{0, 1, 0, -1}
	for scanner.Scan() {
		values := strings.Split(scanner.Text(), "")
		C = len(values)
		for col, v := range values {
			i, _ := strconv.Atoi(v)
			p := point{x: col, y: R}
			G[p] = i
		}
		R++
	}

	for row := 0; row < R; row++ {
		for col := 0; col < C; col++ {
			low := true
			p := point{x: col, y: row}
			for i := 0; i < 4; i++ {
				pTest := point{x: dx[i] + col, y: dy[i] + row}
				if pTest.x >= 0 && pTest.x < C && pTest.y >= 0 && pTest.y < R && G[pTest] <= G[p] {
					low = false
					break
				}
			}
			if low {
				lows = append(lows, p)
				A += G[p] + 1
			}
		}
	}
	fmt.Println("Answer A:", A)

	B := make([]int, 0)
	for _, low := range lows {
		Q, basin := []point{low}, make(map[point]int)
		for len(Q) > 0 {
			pos := Q[0]
			Q = Q[1:]
			basin[pos]++
			for i := 0; i < 4; i++ {
				c, r := pos.x+dx[i], pos.y+dy[i]
				pTest := point{x: c, y: r}
				if c >= 0 && c < C && r >= 0 && r < R && basin[pTest] == 0 && G[pTest] != 9 {
					Q = append(Q, pTest)
				}
			}
		}
		B = append(B, len(basin))
	}
	sort.Ints(B)
	fmt.Println("Answer B:", B[len(B)-3]*B[len(B)-2]*B[len(B)-1])
}
