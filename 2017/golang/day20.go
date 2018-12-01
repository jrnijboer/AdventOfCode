package main

import (
	"fmt"
	"bufio"
	"os"
	"regexp"
	"strconv"
)

func main() {
	file, _ := os.Open("day20.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	positions := make(map[int][]int)
	velocities := make(map[int][]int)
	accelerations := make(map[int][]int)
	particles := []int{}
	p := 0
	for scanner.Scan() {
		line  := scanner.Text()
		var re = regexp.MustCompile(`^\w=<(-?\d+),(-?\d+),(-?\d+)>, \w=<(-?\d+),(-?\d+),(-?\d+)>, \w=<(-?\d+),(-?\d+),(-?\d+)>`)
		groups := re.FindStringSubmatch(line)
		if len(groups) < 10 {
			fmt.Printf("line has %v groups\n", len(groups))
			panic("regex broken")
		}

		x,y,z := getValues(groups[1], groups[2], groups[3])
		vx,vy,vz := getValues(groups[4], groups[5], groups[6])
		ax,ay,az := getValues(groups[7], groups[8], groups[9])

		positions[p] = []int {x,y,z}
		velocities[p] = []int {vx,vy,vz}
		accelerations[p] = []int {ax,ay,az}
		particles = append(particles, p)
		p++
	}
	solveA(positions, velocities, accelerations)
	solveB(particles, positions, velocities, accelerations)
}

func getValues(sX string, sY string, sZ string) (int, int, int) {
	x, _ := strconv.Atoi(sX)
	y, _ := strconv.Atoi(sY)
	z, _ := strconv.Atoi(sZ)
	return x,y,z
}

func solveB(particles []int, positions map[int] []int, velocities map[int] []int, accelerations map[int] []int) {
	iterations := 0
	for iterations < 100 {
		particlePositions := make(map[string][]int)
		for _, p := range particles {
			for i := 0; i < 3; i++ {
				velocities[p][i] += accelerations[p][i]
				positions[p][i] += velocities[p][i]
			}
			s := strconv.Itoa(positions[p][0]) + "," + strconv.Itoa(positions[p][1]) + "," + strconv.Itoa(positions[p][2])
			particlePositions[s] = append(particlePositions[s], p)
		}
		remainingParticles := []int{}

		for _, v := range particlePositions {
			if len(v) == 1 {
				remainingParticles = append(remainingParticles, v[0])
			}
		}
		if len(particles) != len(remainingParticles) {
			iterations = 0
		} else {
			iterations++
		}
		particles = remainingParticles
	}
	fmt.Printf("answer b: %v\n", len(particles))
}

func solveA(positions map[int] []int, velocities map[int] []int, accelerations map[int] []int) {
	min := 1000000
	minP := -1

	for p, v := range accelerations {
		_, m := MinMax(v)
		if m < min {
			min = m
			minP = p
		}
	}
	fmt.Printf("answer a: %v\n", minP)
}

func MinMax(array []int) (int, int) {
	arr := make([]int, len(array))
	copy(arr, array)
	if arr[0] < 0 {
		arr[0] = -arr[0]
	}
	var max int = arr[0]
	var min int = arr[0]
	for _, value := range arr {
		if value < 0  {
			value = -value
		}
		if max < value {
			max = value
		}
		if min > value {
			min = value
		}
	}
	return min, max
}
