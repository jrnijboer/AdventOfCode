package main

import "unicode"

func SumIntSlice(intSlice []int) int {
	sum := 0
	for _, v := range intSlice {
		sum += v
	}
	return sum
}

func MinFromIntSlice(intSlice []int) int {
	min := intSlice[0]
	for _, v := range intSlice {
		if v < min {
			min = v
		}
	}
	return min
}

func MaxFromIntSlice(intSlice []int) int {
	max := intSlice[0]
	for _, v := range intSlice {
		if v > max {
			max = v
		}
	}
	return max
}

func ContainsInt(intSlice []int, value int) bool {
	for _, v := range intSlice {
		if v == value {
			return true
		}
	}
	return false
}

func ContainsString(stringSlice []string, value string) bool {
	for _, v := range stringSlice {
		if v == value {
			return true
		}
	}
	return false
}

func IsUpper(s string) bool {
	for _, r := range s {
		if !unicode.IsUpper(r) && unicode.IsLetter(r) {
			return false
		}
	}
	return true
}

func IsLower(s string) bool {
	for _, r := range s {
		if !unicode.IsLower(r) && unicode.IsLetter(r) {
			return false
		}
	}
	return true
}
