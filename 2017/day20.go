package main
import (
	"fmt"
	"bufio"
	"os"
	"regexp"
	"strconv"
)

func main() {
	//file, _ := os.Open("day20.input.sample")
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
		//fmt.Printf("Line: [%v]\n", line)
		var re = regexp.MustCompile(`^\w=<(-?\d+),(-?\d+),(-?\d+)>, \w=<(-?\d+),(-?\d+),(-?\d+)>, \w=<(-?\d+),(-?\d+),(-?\d+)>`)
		groups := re.FindStringSubmatch(line)
		if len(groups) < 10 {
			fmt.Printf("line has %v groups\n", len(groups))
			panic("regex broken")
		}

		x,_ := strconv.Atoi(groups[1])
		y,_ := strconv.Atoi(groups[2])
		z,_ := strconv.Atoi(groups[3])

		vx,_ := strconv.Atoi(groups[4])
		vy,_ := strconv.Atoi(groups[5])
		vz,_ := strconv.Atoi(groups[6])

		ax,_ := strconv.Atoi(groups[7])
		ay,_ := strconv.Atoi(groups[8])
		az,_ := strconv.Atoi(groups[9])

		positions[p] = []int {x,y,z}
		velocities[p] = []int {vx,vy,vz}
		accelerations[p] = []int {ax,ay,az}
		particles = append(particles, p)
		p++
	}
	solveA(positions, velocities, accelerations)
	solveB(particles, positions, velocities, accelerations)
}

func solveB(particles []int, positions map[int] []int, velocites map[int] []int, accelerations map[int] []int) {
	fmt.Println("B")
}

func solveA(positions map[int] []int, velocites map[int] []int, accelerations map[int] []int) {
	min := 1000000
	minP := -1

	for p, v := range accelerations {
		_, m := MinMax(v)
		if m < min {
			//fmt.Printf("lower acceleration %v found, was: %v, now: %v\n", m, accelerations[minP], accelerations[p])
			min = m
			minP = p
		}
	}
	fmt.Printf("answer a: %v\n", minP)
}

func MinMax(array []int) (int, int) {
	if array[0] < 0 {
		array[0] = -array[0]
	}
	var max int = array[0]
	var min int = array[0]
	for _, value := range array {
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
/*
// A data structure to hold a key/value pair.
type Pair struct {
	Key string
	Value int
}

// A slice of Pairs that implements sort.Interface to sort by Value.
type PairList []Pair

func (p PairList) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p PairList) Len() int {
	return len(p)
}

func (p PairList) Less(i, j int) bool {
	return p[i].Value < p[j].Value
}

// A function to turn a map into a PairList, then sort and return it. 
func sortMapByValue(m map[string]int) PairList {
	p := make(PairList, len(m))
	i := 0
	for k, v := range m {
		p[i] = Pair{k, v}
	}
	sort.Sort(p)
	return p
}
*/
