package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
	"math"
)

var answer = 0
func main() {
	solveA("day23.input")
	solveB("day23.input.optimized")
}

/*
func solveC() {
	comps := 0
	for b := 107900; b <= 124900; b += 17 {//loop 1001 {
		if !isPrime(b) {
			comps++
		}
	}
	fmt.Println("composite numbers: ", comps)

}
*/

func getInstructions(inputfile string) map[int]string {
	file, _ := os.Open(inputfile)
        defer file.Close()
        scanner := bufio.NewScanner(file)
	instructions := make(map[int]string)
	i := 0
	for scanner.Scan() {
		instructions[i] = scanner.Text()
		i++;
	}
	return instructions
}


func solveB(file string) {
	instructions := getInstructions(file)
	pos := 0
	registers := make(map[string]int64)
	registers["a"] = 1
	for pos >= 0 {
		pos = doInstruction(instructions[pos], pos, registers)
	}
	fmt.Printf("b: %v\n", registers["h"])
}

func solveA(file string) {
	instructions := getInstructions(file)
	pos := 0
	registers := make(map[string]int64)
	for pos >= 0 {
		pos = doInstruction(instructions[pos], pos, registers)
	}
	fmt.Printf("a: %v\n", answer)
}

func doInstruction(instruction string, pos int, registers map[string] int64) int {
	s := strings.Split(instruction, " ")
	switch(s[0]) {
		case "set": return doSet(s[1], s[2], registers, pos)
		case "sub": return doSub(s[1], s[2], registers, pos)
		case "mul": return doMul(s[1], s[2], registers, pos)
		case "jnz": return doJnz(s[1], s[2], registers, pos)
		case "nop": return pos + 1
		case "prm": return doPrm(s[1], s[2], registers, pos)
		default: {
			fmt.Printf("unknown instruction: %v\n", s);
			return -1
			//panic("crash and burn")
		}
	}
}

func doPrm(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)

	if isPrime(int(v)) {
		registers[register] = 1
	} else {
		registers[register] = 0
	}
	return pos + 1
}


func isPrime(value int) bool {
	if value % 2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Floor(math.Sqrt(float64(value)))); i+=2 {
		if value % i == 0 {
			return false
		}
	}
	return value > 1
}


func getValue(value string, registers map[string]int64) int64 {
	v, err := strconv.ParseInt(value, 10, 64)
	if err == nil {
		return v
	} else {
		return registers[value]
	}
}


func doSet(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] = v
	return pos + 1

}

func doSub(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] -= v
	return pos + 1

}

func doMul(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] *= v
	answer++
	return pos + 1
}

func doJnz(register string, value string, registers map[string]int64, pos int) int {
	r := getValue(register, registers)
	v := getValue(value, registers)
	if r != 0 {
		return pos + int(v)
	} else {
		return pos + 1
	}
}
