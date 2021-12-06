package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func Day03() {
	file, _ := os.Open("../input/day03.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	input, mostcommon := make([]string, 0), make([]string, 0)

	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	for i := 0; i < len(input[0]); i++ {
		mostcommon = append(mostcommon, get_most_common_bit(input, i))
	}
	gamma, _ := strconv.ParseInt(strings.Join(mostcommon, ""), 2, 32)
	epsilon := int(math.Pow(2, float64(len(input[0])))) - int(gamma) - 1
	fmt.Println("Answer A:", int(gamma)*epsilon)

	oxygen, co2 := make([]string, len(input)), make([]string, len(input))
	copy(oxygen, input)
	copy(co2, input)

	for i := 0; i < len(input[0]); i++ {
		if len(oxygen) > 1 {
			common_oxygen := get_most_common_bit(oxygen, i)
			var tmp []string
			for _, o := range oxygen {
				if string(o[i]) == common_oxygen {
					tmp = append(tmp, o)
				}
			}
			oxygen = tmp
		}
		if len(co2) > 1 {
			common_co2 := get_most_common_bit(co2, i)
			var tmp []string
			for _, c := range co2 {
				if string(c[i]) != common_co2 {
					tmp = append(tmp, c)
				}
			}
			co2 = tmp
		}
	}
	co2int, _ := strconv.ParseInt(strings.Join(co2, ""), 2, 32)
	oxygenint, _ := strconv.ParseInt(strings.Join(oxygen, ""), 2, 32)

	fmt.Println("Answer B:", oxygenint*co2int)
}

func get_most_common_bit(input []string, pos int) string {
	ones := 0
	for _, line := range input {
		if string(line[pos]) == "1" {
			ones++
		}
	}
	if ones >= len(input)-ones {
		return "1"
	}
	return "0"
}
