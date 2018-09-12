package main
import (
        "fmt"
        "bufio"
        "os"
)

func main() {
	file, _ := os.Open("day09.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input := scanner.Text()
		solve(input)
	}
}

func solve(input string){
	length := len(input)
	openbraces := 0
	pos := 0
	garbage := false
	sum := 0
	garbageSum := 0
	for pos < length {
		if garbage && string(input[pos]) != "!" { garbageSum++ }

		switch(string(input[pos])) {
			case "!" : if garbage { pos++ }
			case "<" : garbage = true
			case ">" :
				garbage = false
				garbageSum--
			case "{" : if !garbage { openbraces++ }
			case "}" : if !garbage {
					sum += openbraces
					openbraces--
				}
		}
		pos++
	}

	fmt.Printf("score: %v, garbage: %v\n", sum, garbageSum)
}
