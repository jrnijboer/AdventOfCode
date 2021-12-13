package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type caveCrawler struct {
	pos       string
	smallSeen []string
	twice     bool
}

func solveDay12(N map[string][]string, allowTwice bool) int {
	routeCount := 0
	Q := []caveCrawler{{pos: "start", smallSeen: make([]string, 0), twice: false}}
	for len(Q) > 0 {
		crawler := Q[len(Q)-1]
		Q = Q[:len(Q)-1]
		if crawler.pos == "end" {
			routeCount++
		} else {
			for _, n := range N[crawler.pos] {
				sNext := make([]string, len(crawler.smallSeen))
				copy(sNext, crawler.smallSeen)
				if n != "start" && !ContainsString(crawler.smallSeen, n) {
					if IsLower(n) {
						sNext = append(sNext, n)
					}
					Q = append(Q, caveCrawler{pos: n, smallSeen: sNext, twice: crawler.twice})
				} else if ContainsString(crawler.smallSeen, n) && !crawler.twice && n != "start" && n != "end" && allowTwice {
					Q = append(Q, caveCrawler{pos: n, smallSeen: sNext, twice: true})
				}
			}
		}
	}
	return routeCount
}

func Day12() {
	file, _ := os.Open("../input/day12.input")
	defer file.Close()
	N := make(map[string][]string)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), "-")
		a, b := parts[0], parts[1]
		N[a] = append(N[a], b)
		N[b] = append(N[b], a)
	}
	fmt.Println("Answer A:", solveDay12(N, false))
	fmt.Println("Answer B:", solveDay12(N, true))
}
