package main
import (
        "fmt"
)

func main() {
	a := 277
	b := 349

	factorA := 16807
	factorB := 48271
	solveA(int64(a), int64(b), int64(factorA), int64(factorB))
	solveB(int64(a), int64(b), int64(factorA), int64(factorB))
}

func solveA(a int64, b int64, factorA int64, factorB int64) {
	matches := 0
	for i:= 0; i < 40000000; i++ {
		a = (a * factorA) % 2147483647
		b = (b * factorB) % 2147483647
		if a & 0xFFFF == b & 0xFFFF {
			matches++
		}
	}

	fmt.Printf("matches: %v\n", matches)
}

func solveB(a int64, b int64, factorA int64, factorB int64) {
	matches := 0
	for i := 0; i < 5000000; i++ {
		for ;; {
			a = (a * factorA) % 2147483647
			if a % 4 == 0 {
				break
			}
		}

		for ;; {
			b = (b * factorB) % 2147483647
			if b % 8 == 0 {
				break
			}
		}
		if a & 0xFFFF == b & 0xFFFF {
			matches++
		}
	}
	fmt.Printf("B: %v\n", matches)
}

