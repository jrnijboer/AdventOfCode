package main
import (
        "fmt"
        "bufio"
        "os"
	"strings"
	"strconv"
	"encoding/hex"
)

func main() {
	file, _ := os.Open("day10.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		s := strings.Split(line, ",")
		input := []byte{}
		for _, v := range(s) {
			v = strings.TrimSpace(v)
			i,_ := strconv.Atoi(v)
			input = append(input, byte(i))
		}
		inputBytes := []byte{}
		for i := 0; i < len(line); i++ {
			inputBytes = append(inputBytes,line[i])
		}
		hashA := knotHash(input, 256, 1)
		fmt.Printf("Part a: %v\n", int(hashA[0]) * int(hashA[1]))
		hashB := solveB(inputBytes, 256)
		fmt.Printf("Part b: %v\n", hashB)
	}
}

func solveB(input []byte, hashsize int) string{
	input = append(input, 17, 31, 73, 47, 23)
	sparseHash := knotHash(input, hashsize, 64)
	return getDenseHash(sparseHash)
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

func knotHash(input []byte, hashsize int, runs int) []byte {
	skip := 0
	pos := 0
	hash := []byte{}
	for i := 0; i <= hashsize - 1; i++ {
		hash = append(hash,byte(i))
	}

	for i:= 0; i < runs; i++ {
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
