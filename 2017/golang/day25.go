package main
import (
	"fmt"
)

func main() {
	state := "a"
	position := 0
	tape := make(map[int]bool)
	solve(state, position, tape, 12667664)
}

func solve(state string, position int, tape map[int]bool, steps int) {
	for steps > 0 {
		switch state {
			case "a": state, position, tape = stateA(position, tape)
			case "b": state, position, tape = stateB(position, tape)
			case "c": state, position, tape = stateC(position, tape)
			case "d": state, position, tape = stateD(position, tape)
			case "e": state, position, tape = stateE(position, tape)
			case "f": state, position, tape = stateF(position, tape)
		}
		steps--
	}
	result := 0
	for _,v := range tape {
		if v {
			result++
		}
	}
	fmt.Printf("answer: %v\n", result)
}

func stateA(pos int, tape map[int]bool) (string, int, map[int]bool){
	var nextstate string
	p := pos
	if !tape[pos] {
		pos++
		nextstate = "b"
	} else {
		pos--
		nextstate = "c"
	}
	tape[p] = !tape[p]
	return nextstate, pos, tape
}

func stateB(pos int, tape map[int]bool) (string, int, map[int]bool){
	var nextstate string
	if !tape[pos] {
		tape[pos] = !tape[pos]
		pos--
		nextstate = "a"
	} else {
		pos++
		nextstate = "d"
	}
	return nextstate, pos, tape
}

func stateC(pos int, tape map[int]bool) (string, int, map[int]bool){
	var nextstate string
	if !tape[pos] {
		pos--
		nextstate = "b"
	} else {
		tape[pos] = !tape[pos]
		pos--
		nextstate = "e"
	}
	return nextstate, pos, tape
}

func stateD(pos int, tape map[int]bool) (string, int, map[int]bool){
	var nextstate string
	p := pos
	if !tape[pos] {
		pos++
		nextstate = "a"
	} else {
		pos++
		nextstate = "b"
	}
	tape[p] = !tape[p]
	return nextstate, pos, tape
}

func stateE(pos int, tape map[int]bool) (string, int, map[int]bool){
	var nextstate string
	if !tape[pos] {
		tape[pos] = !tape[pos]
		pos--
		nextstate = "f"
	} else {
		pos--
		nextstate = "c"
	}
	return nextstate, pos, tape
}

func stateF(pos int, tape map[int]bool) (string, int, map[int]bool){
	var nextstate string
	if !tape[pos] {
		tape[pos] = !tape[pos]
		pos++
		nextstate = "d"
	} else {
		pos--
		nextstate ="a"
	}
	return nextstate, pos, tape
}
