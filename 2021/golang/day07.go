package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strconv"
	"strings"
)

func Day07() {
	bytes, _ := ioutil.ReadFile("../input/day07.input")
	A, B, crabs := 0, 0, make([]int, 0)
	for _, v := range strings.Split(string(bytes), ",") {
		n, _ := strconv.Atoi(v)
		crabs = append(crabs, n)
	}
	sort.Ints(crabs)

	sum, median := 0, crabs[(len(crabs)-1)/2]
	for _, v := range crabs {
		sum += v
	}
	avg := float64(sum) / float64(len(crabs))
	P := []int{int(math.Floor(avg)), int(math.Ceil(avg))}

	for _, v := range crabs {
		d := median - v
		if d < 0 {
			d *= -1
		}
		A += d
	}
	for _, p := range P {
		b := 0
		for _, v := range crabs {
			d := p - v
			if d < 0 {
				d *= -1
			}
			b += d * (d + 1) / 2
		}
		if B == 0 || b < B {
			B = b
		}
	}
	fmt.Println("Answer A:", A)
	fmt.Println("Answer B:", B)
}
