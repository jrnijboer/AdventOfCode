package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main() {
	//promenade := []rune("abcde")
	input := "abcdefghijklmnop"

	file, _ := os.Open("day16.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		res := solve(line, input, 1)
		fmt.Printf("Part a: %v\n", string(res))
		res = solve(line, res, 1000000000)
		fmt.Printf("Part b: %v\n", string(res))
	}
}

func solve(line string, input string, loops int) string{
	instructions := strings.Split(line, ",")
	promenade := []rune(input)
	cycle := 1

	for cycle <= loops {
		for _, instruction := range instructions {
			if instruction[0] == 's' {
				position, _ := strconv.Atoi(instruction[1:])
				promenade = spin(promenade, position)
			} else if  instruction[0] == 'x' {
				params := strings.Split(instruction[1:],"/")
				a, _ := strconv.Atoi(params[0])
				b, _ := strconv.Atoi(params[1])
				promenade = exchange(promenade, a, b)
			} else if instruction[0] == 'p' {
				params := []rune(string(instruction[1:]))
				promenade = partner(promenade, rune(params[0]), rune(params[2]))
			}
		}
		if string(promenade) == "jkmflcgpdbonihea" && cycle > 1 {
			fmt.Printf("repetition found after %v cycles\n", cycle)
			return solve(line, string(promenade), 1000000000 % (cycle) - 1)
			//break
		}
		cycle++
	}
	return string(promenade)
}

func spin(promenade []rune, x int) []rune {
	result := promenade[len(promenade)-x:]
	result = append(result, promenade[:len(promenade)-x]...)
	promenade = result;
	return result
}

func exchange(promenade []rune, a int, b int) []rune {
	promenade[a], promenade[b] = promenade[b], promenade[a]
	return promenade
}

func partner(promenade []rune, a rune, b rune) []rune {
	posA := getIndex(promenade, a)
	posB := getIndex(promenade, b)
	exchange(promenade, posA, posB)
	return promenade
}

func getIndex(promenade []rune, r rune) int {
	for i := 0;;i++ {
		if promenade[i] == r {
			return i
		}
	}
	panic("not gonna happen")
}

