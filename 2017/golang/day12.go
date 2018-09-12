package main
import (
        "fmt"
        "bufio"
        "os"
	"strings"
	"strconv"
)

func main() {
	file, _ := os.Open("day12.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	gates := make(map[int] []int)
	var gatesList []int
	gatesToDest := make(map[int] byte) //0 is unknown, 1 is confirmed gate to zero, 2 is visited and unknown
	dest := 0
	sumA := 0
	countB := 0

	for scanner.Scan() {
		line := scanner.Text()
		input := strings.Split(line, " <-> ")
		var destinations []int
		source, _ := strconv.Atoi(input[0])
		for _,i := range strings.Split(input[1], ", ") {
			val, _ := strconv.Atoi(i)
			destinations = append(destinations,val)
		}
		gates[source] = destinations
		gatesToDest[source] = 0
		gatesList = append(gatesList, source)
	}

	for dest != 2000000 {
		nextGates := make(map[int] []int)
		nextGatesToDest := make(map[int] byte)
		gatesToDest[0] = 1
		var callstack []int
		solve(dest, gatesList, gates, gatesToDest, dest, callstack)
		nextDest := 2000000
		for k, v := range gatesToDest {
			if v == 1 && dest == 0 {
				sumA++
			} else if v == 2 {
				if k < nextDest {
					nextDest = k
				}
				nextGates[k] = gates[k]
				nextGatesToDest[k] = 0
			}
		}
		dest = nextDest
		gates = nextGates
		gatesToDest = nextGatesToDest
		countB++
	}

	fmt.Printf("Answer part A: %v\n", sumA)
	fmt.Printf("Answer part B: %v\n", countB)
}

func solve(dest int, gatesList []int, gatesDict map[int][]int, gatesToDest map[int] byte, start int, callstack []int) {
	for i := start; i < start + len(gatesList); i++ {
		gate := gatesList[i % len(gatesList)]
		destinations := gatesDict[gate]
		if gatesToDest[gate] != 1 {
			for _, destination := range destinations {
				if destination == dest || gatesToDest[destination] == 1 {
					callstack = append(callstack, gate)
					callstack = append(callstack, destinations...)
					for _, g := range callstack {
						gatesToDest[g] = 1
					}
					callstack = nil
					break
				} else if gatesToDest[gate] == 0 {
					gatesToDest[gate] = 2
					solve(dest, gatesList, gatesDict, gatesToDest, destination, append(callstack, gate))
				} else if gatesToDest[gate] == 2 {
					callstack = nil
				}
			}
		}
	}
}
