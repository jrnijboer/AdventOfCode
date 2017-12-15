package main
import (
        "fmt"
	"strings"
	"strconv"
	"encoding/hex"
)

type Point struct {
	x int
	y int
}

func main() {
	bytes := []byte("vbqugkhl-")
	bits := 0
	grid := make([][]bool, 128)
	for i := range grid {
	    grid[i] = make([]bool, 128)
	    }

	for i:= 0; i < 128; i++ {
		val := []byte(strconv.Itoa(i))
		row := bytes
		for _, v := range val {
			row = append(row, v)
		}
		hashBytes := knotHash(row)
		hash := getDenseHash(hashBytes)
		bits += getPopCount(hash)
		for k, v := range getBinaryString(hash) {
			grid[i][k] = v == '1'
		}
	}
	fmt.Printf("popcount: %v\n", bits)
	fmt.Printf("Regions: %v\n", getRegions(grid))
}

func getRegions (grid [][]bool) int {
	regions := 0
	for y := 0; y < 128; y++ {
		for x:= 0; x < 128; x++ {
			if grid[y][x] {
				grid[y][x] = false
				fillRegion(grid, Point {x, y})
				regions++
			}
		}
	}
	return regions
}

func fillRegion(grid [][]bool, p Point) {
	directions := []Point{ Point{0,1}, Point{1,0}, Point{-1, 0}, Point{0, -1}}

	for _, v := range directions {
		x := p.x + v.x
		y := p.y + v.y
		if 0 <= x && x < 128 && 0 <= y && y < 128 && grid[y][x]{
			grid[y][x] = false
			fillRegion(grid, Point {x, y})
		}
	}
}

func zeroPad(s string, length int) string {
	var pads int
	pads = length - len(s)
	return strings.Repeat("0", pads) + s
}

func getPopCount(hash string) int {
	popcount := 0
	for _, v := range strings.Split(hash, "") {
		arr, _ := hex.DecodeString("0" + v)
		b := byte(arr[0])
		var c int
		for c = 0; b > 0; c++ {
			b &= b - 1
		}
		popcount += c
	}
	return popcount
}

func getBinaryString(hash string) string {
	var output string
	for _, v := range(strings.Split(hash, "")) {
		arr, _ := hex.DecodeString("0" + v)
		b := arr[0]
		output += zeroPad(strconv.FormatInt(int64(b), 2), 4)
	}
	return output
}

func getDenseHash(input []byte) string {
	var dense [16]byte
	for i := 0; i < 16; i++ {
		value := byte(0)
		for j := 0; j < 16; j++ {
			value ^= input[(i*16) + j]
		}
		dense[i] = value
	}
	return hex.EncodeToString(dense[:])
}

func knotHash(input []byte) []byte {
	skip := 0
	pos := 0
	input = append(input, 17, 31, 73, 47, 23)
	hash := []byte{}
	for i := 0; i < 256; i++ {
		hash = append(hash,byte(i))
	}

	for i:= 0; i < 64; i++ {
		for _, v := range(input) {
			reverse := getReverseSubrange(hash,pos, v)
			for key, val := range(reverse) {
				hash[(key + pos) % len(hash)] = val
			}
			pos = (pos + int(v) + skip) % len(hash)
			skip++
		}
	}
	return hash
}

func getReverseSubrange(hash []byte, pos int, size byte ) []byte {
	subrange := []byte{}
	for i:= pos + int(size) - 1; i >= pos; i-- {
		subrange = append(subrange, hash[i%len(hash)])
	}
	return subrange
}
