package main
import (
	"fmt"
	"strconv"
	"strings"
	"io/ioutil"
) 

func main() { 
	input, _ := ioutil.ReadFile("../input/day1.input")
	fA, fB := 0, 0
	for _, line := range strings.Split(string(input), "\n") {
		input, _ := strconv.Atoi(line)
		fuel := input / 3 - 2
		fA += fuel
		for fuel > 0 {
        	fB += fuel
			fuel = fuel/3 - 2
		}		
	}
	fmt.Printf("answer a: %v\n", fA)
	fmt.Printf("answer b: %v\n", fB)
}