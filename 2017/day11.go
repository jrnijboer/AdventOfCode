package main
import (
        "fmt"
        "bufio"
        "os"
	"strings"
)

func main() {
	file, _ := os.Open("day11.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		input := strings.Split(line, ",")
		solve(input)
	}
}

func solve(input []string) {
	x:= 0
	y:= 0
	max := 0
	for _,v := range (input) {
		switch(v) {
			case "n": y += 2
			case "ne": y++; x++;
			case "se": y--; x++;
			case "s": y -= 2
			case "sw": y--; x--;
			case "nw": y++; x--;
			default: panic("unknown direction")
		}
		d := getDistance(x,y)
		if d > max {
			max = d
		}
	}
	fmt.Printf("finished at postion x: %v, y: %v\n", x, y)
	fmt.Printf("part a: %v\n", getDistance(x,y))
	fmt.Printf("part b: %v\n", max)
}

func getDistance(x int, y int) int {
	if x < 0 {
		x *= -1
	}
	if y < 0 {
		y *= -1
	}
	if x > y {
		return x
	} else {
		distance := 0
		distance += x;
		y -= x
		distance += y/2
		return distance
	}
}
