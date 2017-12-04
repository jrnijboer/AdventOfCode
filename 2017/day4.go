package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"sort"
)

func main() {
	validLinesA := 0
	validLinesB := 0
	file, _ := os.Open("day4.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if passwordlineIsValid(line, false) {
			validLinesA++
		}
		if passwordlineIsValid(line, true) {
			validLinesB++
		}
	}
	fmt.Printf("Valid lines for part A is %v\n", validLinesA)
	fmt.Printf("Valid lines for part B is %v\n", validLinesB)
}

func passwordlineIsValid(input string, checkAnagrams bool) bool {
	arr := strings.Split(input, " ")
	if checkAnagrams {
		var sortedPasswords = []string{}
		for k := 0; k < len(arr); k++ {
			sortedPasswords = append(sortedPasswords, SortString(arr[k]))
		}
		arr = sortedPasswords
	}


	for i := 0; i < len(arr) - 1; i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[j] == arr[i] {
				return false
			}
		}
	}
	return true
}

//https://stackoverflow.com/a/22689818
func SortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}
