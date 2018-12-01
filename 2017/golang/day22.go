package main
import (
	"fmt"
	"bufio"
	"os"
	"math"
)

type Point struct {
	x int
	y int
}

func main() {
	file, _ := os.Open("day22.input")
        fi,_ := file.Stat()
	size := fi.Size()
	dimension := int(math.Sqrt(float64(size))) / 2 //this calculation is iffy

	defer file.Close()
        scanner := bufio.NewScanner(file)
	gridA := make(map[Point] bool)
	gridB := make(map[Point] byte)
	y := dimension

	for scanner.Scan() {
		x := dimension * -1
		line  := scanner.Text()
		for c := range line {
			p := Point{x, y}
			x++
			if string(line[c]) == "#" {
				gridA[p] = true
				gridB[p] = 2
			}
		}
		y--
	}
	solveA(gridA)
	solveB(gridB)
}

func solveB(grid map[Point]byte) {
	infected := 0
	directions := []Point{ Point{0,1}, Point{1,0}, Point{0, -1}, Point{-1, 0}}
	direction := 0
	position := Point{0, 0}
	for i:= 0; i < 10000000; i++ {
		if grid[position] == 0{//clean
			direction = (direction - 1 + 4) % 4
		} else if grid[position] == 1 {//weak
			infected++
		} else if grid[position] == 2 {//infected
			direction = (direction + 1) % 4
		} else if grid[position] == 3 {//flagged
			direction = (direction + 2) % 4
		}
		grid[position] = (grid[position] + 1) % 4
		position.x += directions[direction].x
		position.y += directions[direction].y
	}
	fmt.Printf("answer b: %v infected: \n", infected)
}

func solveA(grid map[Point]bool) {
	infected := 0
	directions := []Point{ Point{0,1}, Point{1,0}, Point{0, -1}, Point{-1, 0}}
	direction := 0
	position := Point{0, 0}
	for i:= 0; i < 10000; i++ {
		if grid[position] {
			direction = (direction + 1 + 4) % 4
		} else {
			infected++
			direction = (direction - 1 + 4) % 4
		}
		grid[position] = !grid[position]
		position.x += directions[direction].x
		position.y += directions[direction].y
	}
	fmt.Printf("answer a: %v infected: \n", infected)
}

