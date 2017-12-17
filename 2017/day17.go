package main
import (
	"fmt"
)

func main() {
	input := 386
	solveA(input)
	solveB(input)
}

func solveA(stepsize int) {
	pos := 0
	spinlocks := []int { 0 }
	for i := 1; i <= 2017 ; i++ {
		pos = (pos + stepsize) % i + 1
		spinlocks = append(spinlocks, 0)
		copy(spinlocks[pos+1:], spinlocks[pos:])
		spinlocks[pos] = i
	}
	fmt.Printf("answer a: %v\n", spinlocks[pos+1])

}

func solveB(stepsize int) {
	pos := 0
	v := 0
	for i := 1; i <= 50000000 ; i++ {
		pos = (pos + stepsize) % i + 1
		if pos == 1 {
			v = i
		}
	}
	fmt.Printf("answer b: %v\n", v)
}

