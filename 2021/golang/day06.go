package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func solveDay6(fish []string, days int) int {
	sum, F := 0, make(map[int]int)
	for _, f := range fish {
		ix, _ := strconv.Atoi(f)
		F[ix]++
	}
	for i := 1; i <= days; i++ {
		spawns, Fnew := F[0], make(map[int]int)
		for j := 0; j < 8; j++ {
			Fnew[j] = F[j+1]
		}
		Fnew[6], Fnew[8] = Fnew[6]+spawns, F[0]
		F = Fnew
	}
	for _, v := range F {
		sum += v
	}
	return sum
}

func Day06() {
	b, _ := ioutil.ReadFile("../input/day06.input")
	fmt.Println("Answer A:", solveDay6(strings.Split(string(b), ","), 80))
	fmt.Println("Answer B:", solveDay6(strings.Split(string(b), ","), 256))
}
