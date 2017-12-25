package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"math"
)

func main() {
	file, _ := os.Open("day21.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	enhancements := make(map[string]string)
	for scanner.Scan() {
		line := scanner.Text()
		s := strings.Split(line, " => ")
		enhancements[s[0]] = s[1]
	}
	grid := []string{".#.", "..#", "###"}
	solve(grid, enhancements, 5)
	solve(grid, enhancements, 18)
}

func solve(grid []string, enhancements map[string]string, iterations int) {
	for iterations > 0 {
		grid = enhance(grid, enhancements)
		iterations--
	}
	enabled := 0
	for i := range grid {
		for j := range grid[i] {
			if string(grid[i][j]) == "#" {
				enabled++
			}
		}
	}
	fmt.Printf("answer: %v\n", enabled)
}

func enhance(grid []string, enhancements map[string]string) []string {
	squares := getSquaresFromGrid(grid)
	for i := range squares {
		square := squares[i]
		var s string
		for k:= 0; k < 9; k++ {
			s = squareToString(square)
			if enhancements[s] != "" {
				square = strings.Split(enhancements[s],"/")
				break
			}
			square = rotateSquare(square)
			if k == 4 {
				square = flipSquare(square)
			}
		}
		squares[i] = strings.Split(enhancements[s], "/")
	}
	grid = buildGridFromSquares(squares)
	return grid
}

func flipSquare(square []string) []string {
	flipped := []string{}
	for row := range square {
		flipped = append(flipped, reverseString(square[row]))
	}
	return flipped
}

func reverseString(s string) string {
	var reverse string
	for i := len(s)-1; i >= 0; i-- {
		reverse += string(s[i])
	}
	return reverse
}

func rotateSquare(square []string) []string {
	rotatedSquare := []string{}
	if len(square[0]) == 2 {
		rotatedSquare = append(rotatedSquare, string(square[1][0]) + string(square[0][0]))
		rotatedSquare = append(rotatedSquare, string(square[1][1]) + string(square[0][1]))
	} else {
		rotatedSquare = append(rotatedSquare, string(square[2][0]) + string(square[1][0]) + string(square[0][0]))
		rotatedSquare = append(rotatedSquare, string(square[2][1]) + string(square[1][1]) + string(square[0][1]))
		rotatedSquare = append(rotatedSquare, string(square[2][2]) + string(square[1][2]) + string(square[0][2]))
	}
	return rotatedSquare
}

func buildGridFromSquares(squares [][]string) []string {
	dim := int(math.Sqrt(float64(len(squares))))
	grid := []string{}
	for y := 0; y < dim; y++ {
		for yRow := 0; yRow < len(squares[y]); yRow++ {
			row := ""
			for x := 0; x < dim; x++ {
				row += squares[y*dim + x][yRow]
			}
			grid = append(grid, row)
		}
	}
	return grid
}

func buildSquareFromString(s string) []string {
	rows := strings.Split(s, "/")
	return rows

}

func squareToString(square []string) string {
	result := ""
	for i := range square {
		result = result + square[i] + "/"
	}
	return result[:len(result)-1]
}

func getSquaresFromGrid(grid []string) [][]string {
	var squares [][]string

	if len(grid[0]) % 2 == 0 {
		for y := 0; y * 2 < len(grid[0]); y++ {
			for x := 0; x * 2 < len(grid[0]); x++ {
				square := []string{}
				square = append(square, string(grid[y*2][x*2]) + string(grid[y*2][x*2+1]))
				square = append(square, string(grid[y*2+1][x*2]) + string(grid[y*2+1][x*2+1]))
				squares = append(squares, square)
			}
		}
	} else {
		for y := 0; y * 3 < len(grid[0]); y++ {
			for x := 0; x * 3 < len(grid[0]); x++ {
				square := []string{}
				square = append(square, string(grid[y*3][x*3]) + string(grid[y*3][x*3+1]) + string(grid[y*3][x*3+2]))
				square = append(square, string(grid[y*3+1][x*3]) + string(grid[y*3+1][x*3+1]) + string(grid[y*3+1][x*3+2]))
				square = append(square, string(grid[y*3+2][x*3]) + string(grid[y*3+2][x*3+1]) + string(grid[y*3+2][x*3+2]))
				squares = append(squares, square)
			}
		}
	}
	return squares
}
