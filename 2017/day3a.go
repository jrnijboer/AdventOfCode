package main

import (
	"fmt"
	"math"
)

func main() {
	solveA(312051)
}

func solveA(input int) {
	
	distanceA := calculateDistance(input)
	fmt.Printf("Answer A: distance from %v to center is %v\n", input, distanceA)
}
func calculateDistance(input int) int {
	ring := getRing(input)
	max := int(math.Pow(float64((2 * (ring + 1)) - 1), 2)) 
	distance := getshortestDistanceToCenterNode(input, ring, max)

	return distance + ring
}

func getRing(input int) int {
	for ring := 0;; ring ++ {
		if int(math.Pow(float64((2 * (ring + 1)) - 1), 2)) >= input {
			return ring 
		}
	}
}

func getCenterNodes(ring int, max int) [4]int {
	var centers [4]int
	if ring == 1 {
		return [4] int {1, 1, 1, 1}
	}
	center := ((ring * 2 + 1) * (ring * 2 + 1)) - ring
	centers[0] = center
	for i := 1; i <= 3; i++ {
		center -= ring * 2
		centers[i] = center
	}

	return centers
}

func getshortestDistanceToCenterNode(input int, ring int, max int) int {
	if ring == 0 {
		return 0
	}
	min := input
	center := ((ring * 2 + 1) * (ring * 2 + 1)) - ring
	for i := 0; i < 4; i++ {
		distance := int(math.Abs(float64(input-center)))
		if distance < min {
			min = distance 
		}
		center -= ring * 2
	}

	return min
}
