package main

import (
	"fmt"
	"strconv"
	"bufio"
	"os"
	"strings"
	"sync"
)

type Checksum struct {
	mutex sync.Mutex
	value int
}

func (c *Checksum) Add (i int) {
	c.mutex.Lock()
	c.value += i
	c.mutex.Unlock()
}

var checksumA Checksum
var checksumB Checksum

var waitgroup sync.WaitGroup

func main() {
	file, _ := os.Open("day2.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		numbers := getNumbersFromLine(scanner.Text())
		waitgroup.Add(2)
		go calculateChecksumA(numbers[:])
		go calculateChecksumB(numbers[:])
	}
	waitgroup.Wait()
	fmt.Printf("Checksum for part A is %v\n", checksumA.value)
	fmt.Printf("Checksum for part B is %v\n", checksumB.value)
}

func getNumbersFromLine(input string) []int {
	arr := strings.Split(input, "\t")
	var numbers = []int{}
	for _, i := range arr {
		n, _ := strconv.Atoi(i)
		numbers = append(numbers,n)
	}
	return numbers
}

func calculateChecksumB(numbers []int) {
	defer waitgroup.Done()
	for i := 0; i < len(numbers); i++ {
		for j := 0; j < len(numbers); j++ {
			if numbers[i] %  numbers[j] == 0 && i != j {
				checksumB.Add(numbers[i] / numbers[j])
				return
			}
		}
	}
	panic("no checksum found")
}

func calculateChecksumA(numbers []int)  {
	defer waitgroup.Done()
	min := 20000000
	max := 0
	for i := 0; i < len(numbers); i++ {
		if numbers[i] > max {
			max = numbers[i]
		}
		if numbers[i] < min {
			min = numbers[i]

		}
	}
	checksumA.Add(max - min)
}
