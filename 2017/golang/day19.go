package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

type Point struct {
	x int
	y int
}

var moves = 0

func main() {
	file, _ := os.Open("day19.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	var grid [][]string
	for scanner.Scan() {
		line  := scanner.Text()
		s := strings.Split(line, "")
		grid = append(grid, s)
	}
	solve(grid)
}

func solve(grid [][]string) {
	y := 0
	var x int
	route := ""
	direction := "down"
	for k, v := range grid[0] {
		if v == "|" {
			x = k
			break
		}
	}
	var letters string
	for direction != "stop" {
		if direction == "down" {
			letters,x,y,direction = move(Point{0, 1}, grid, x, y)
		} else if direction == "up" {
			letters,x,y,direction = move(Point{0, -1}, grid, x, y)
		} else if direction == "left" {
			letters,x,y,direction = move(Point{-1, 0}, grid, x, y)
		} else if direction == "right" {
			letters,x,y,direction = move(Point{1, 0}, grid, x, y)
		}
		route += letters
	}
	fmt.Printf("route: %v\n", route)
	fmt.Printf("total moves: %v\n", moves)
}

func move (direction Point, grid [][]string, x int, y int ) (string, int, int, string) {
	letters := ""

	for ;; {
		y += direction.y
		x += direction.x
		moves++
		if grid[y][x] == "+" || grid[y][x] == " " {
			break
		} else if grid[y][x] != "|" && grid[y][x] != "-" && grid[y][x] != "+" {
			letters += grid[y][x]
		}
	}
	nextDirection := "stop"
	if direction.y != 0  {
		if grid[y][x-1] != " "{
			nextDirection = "left"
		} else if grid[y][x+1] != " " {
			nextDirection = "right"
		}
	} else if direction.x != 0 {
		if grid[y-1][x] != " " {
			nextDirection = "up"
		} else if grid[y+1][x] != " " {
			nextDirection = "down"
		}
	}

	return letters, x, y, nextDirection
}

