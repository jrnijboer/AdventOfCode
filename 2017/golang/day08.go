package main
import (
        "fmt"
        "bufio"
        "os"
        "strconv"
	"regexp"
)

func main() {
	var registers = make(map[string]int)

	file, _ := os.Open("day08.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	maxEver := 0
        for scanner.Scan() {
		instruction := scanner.Text()
		maxEver = DoInstruction(instruction, registers, maxEver)
	}
	max := 0
	for _, v := range registers {
		if v > max {
			max = v
		}
	}
	fmt.Printf("Largest register value currently: %v\n", max)
	fmt.Printf("Max ever was %v\n", maxEver)
}

func DoInstruction(instruction string, registers map[string]int, maxEver int) int {
	re := regexp.MustCompile(`(?P<reg>\S+) (?P<oper>inc|dec) (?P<val>-?\d+) if (?P<reg2>\S+) (?P<comparer>.*) (?P<valreg2>-?\d+)`)
	groups := re.FindStringSubmatch(instruction)
	register := groups[1]
	operator := groups[2]
	value, _ := strconv.Atoi(groups[3])
	valueCheck, _ := strconv.Atoi(groups[6])

	if ShouldExecute(groups[4], groups[5], valueCheck, registers) {
		switch(operator) {
			case "inc" : registers[register] += value
			case "dec" : registers[register] -= value
			default : panic("unknown operator")
		}
	}
	if registers[register] > maxEver {
		return registers[register]
	}
	return maxEver
}

func ShouldExecute(registerCheck string, equalityCheck string, value int, registers map[string]int) bool {
	switch(equalityCheck) {
		case "==": return registers[registerCheck] == value
		case "!=": return registers[registerCheck] != value
		case ">": return registers[registerCheck] > value
		case "<": return registers[registerCheck] < value
		case ">=": return registers[registerCheck] >= value
		case "<=": return registers[registerCheck] <= value
		default: panic("unknown equality check")
	}
	return false
}
