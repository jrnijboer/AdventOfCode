package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)
var max = 0
var maxLength = 0
var maxLengthStrength = 0

type Magnet struct {
	pole1 int
	pole2 int
}

func main() {
	inputfile := "day24.input"
	file, _ := os.Open(inputfile)
        defer file.Close()
        scanner := bufio.NewScanner(file)
	magnets := make(map[int] Magnet)
	i := 0
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), "/")
		v1, _ := strconv.Atoi(s[0])
		v2, _ := strconv.Atoi(s[1])
		magnets[i] = Magnet{v1,v2}
		i++;
	}
	solve(magnets)
}

func solve(magnets map[int]Magnet) {
	next := 0
	bridge := []Magnet{}
	build(magnets, next, bridge)
	fmt.Printf("strongest bridge had strength %v\n", max)
	fmt.Printf("the longest bridge had strength %v\n", maxLengthStrength)

}

func build(availableMagnets map[int] Magnet, next int, bridge []Magnet) {
	magnets := getMagnets(next, availableMagnets)
	if len(magnets) > 0 {
		for k, magnet := range magnets {
			available := make(map[int]Magnet)
			for i,v := range availableMagnets {
				if k != i {
					available[i] = v
				}
			}

			b := make([]Magnet, len(bridge))
			copy(b, bridge)
			b = append(b, magnet)
			var n int
			if magnet.pole1 == next {
				n = magnet.pole2
			} else {
				n = magnet.pole1
			}
			build(available, n, b)
		}
	} else {
		s := getBridgeStrength(bridge)
		if s > max {
			max = s
		}
		if (len(bridge) == maxLength && s > maxLengthStrength) || len(bridge) > maxLength  {
			maxLength = len(bridge)
			maxLengthStrength = s
		}
	}
}

func getMagnets(pins int, available map[int]Magnet) (map[int]Magnet) {
	result := make(map[int]Magnet)
	for k, m := range available {
		if m.pole1 == pins || m.pole2 == pins {
			result[k] = m
		}
	}
	return result
}

func getBridgeStrength(bridge []Magnet) int {
	strength := 0
	for _, v := range(bridge) {
		strength += v.pole1 + v.pole2
	}
	return strength
}

