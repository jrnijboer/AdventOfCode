package main
import (
        "fmt"
        "bufio"
        "os"
	"strings"
	"strconv"
)

func main() {
	file, _ := os.Open("day13.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)

	firewalls := make(map[int]int)
	var firewallsList []int
	last := 0

	for scanner.Scan() {
		line := scanner.Text()
		s := strings.Split(line, ": ")
		pos, _ := strconv.Atoi(s[0])
		strength, _ := strconv.Atoi(s[1])
		firewalls[pos] = strength
		firewallsList = append(firewallsList, pos)
		if pos > last {
			last = pos
		}
	}
	delay := 0
	damage := solveA(firewalls, last, delay)
	fmt.Printf("A, damage without delay: %v\n", damage)
	delay = 2
	for ;; {
		delay+=4
		if solveB(firewalls, last, delay) {
			break
		}
	}
	fmt.Printf("B, no damage after delay %v\n", delay)
}

func solveB(firewalls map[int]int, last int, delay int) bool {
	position := 0

	for position <= last {
		if isCaught(position, firewalls, delay) {
			return false
		}
		position++
	}
	return true
}

func solveA(firewalls map[int]int, last int, delay int) int {
	position := 0
	damage := 0
	for position <= last {
		if isCaught(position, firewalls, delay) {
			damage += position * firewalls[position]
		}
		position++
	}
	return damage
}

func isCaught(pos int, firewalls map[int] int, delay int) bool{
	if firewalls[pos] == 0 {
		return false
	} else {
		fwPos := (pos + delay) % ((firewalls[pos] - 1) * 2)
		return fwPos == 0
	}
}
