package main
import (
        "fmt"
        "bufio"
        "os"
        "strconv"
        "strings"
)

func main() {
        var memory = []int{}
        file, _ := os.Open("day6.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
        for scanner.Scan() {
		line := scanner.Text()
		values := strings.Split(line, "\t")
		for _, val := range values {
			i, _ := strconv.Atoi(val)
			memory = append(memory, i)
		}
        }

        solve(memory)
}

func solve(memory []int) {
	cycles := 0
	states := make(map[string]int)
	for ;; {
		cycles++
		redistribute(memory)
		//fmt.Printf("%v\t- Memory:\t%v\n", i, memory)
		state := ""
		for _, e := range memory {
			c := strconv.Itoa(e)
			state += c + "-"
		}
		if states[state] > 0  {
			fmt.Printf("infinite loop detected after %v cycles\n", cycles)
			fmt.Printf("loop length: %v cycles\n", cycles - states[state])
			break
		}

		states[state] = cycles
	}
}

func redistribute(memory []int) {
	pos := getMaxCellPositionFromMemory(memory)
	value := memory[pos]
	memory[pos] = 0
	for value > 0 {
		memory[(pos+1) % len(memory)]++
		value--
		pos++
	}
}

func getMaxCellPositionFromMemory(memory []int) int {
    max := 0
    pos := 0
    for i, e := range memory {
        if e > max {
            pos = i
            max = e
        }
    }
    return pos
}

