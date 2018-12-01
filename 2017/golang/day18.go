package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

var answer = 0

func main() {
	file, _ := os.Open("day18.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	instructions := make(map[int]string)
	i := 0
	for scanner.Scan() {
		instructions[i] = scanner.Text()
		i++;
	}
	solveA(instructions)
	answer = 0
	solveB(instructions)
}

func solveB(instructions map[int] string) {
	pos0 := 0
	pos1 := 0
	resumeP0 := 0
	resumeP1 := 0
	registers0 := make(map[string]int64)
	registers0["p"] = 0
	registers1 := make(map[string]int64)
	registers1["p"] = 1
	queue0 := []int64{}
	queue1 := []int64{}
	p := 1

	for pos0 >= 0 || pos1 >= 0 {
		if p == 0 {
			resumeP0 = pos0
			pos0, queue0, queue1 = doInstructionB(instructions[pos0], pos0, registers0, queue0, queue1, false)
			if pos0 < 0 {
				p = 1
				if pos1 == -1 && len(queue0) > 0 {
					pos1 = resumeP1
				}
			}
		} else {
			resumeP1 = pos1
			pos1, queue1, queue0 = doInstructionB(instructions[pos1], pos1, registers1, queue1, queue0, true)
			if pos1 < 0 {
				p = 0
				if pos0 == -1 && len(queue1) > 0 {
					pos0 = resumeP0
				}
			}
		}
	}
	fmt.Printf("b: %v\n", answer)
}

func solveA(instructions map[int] string) {
	pos := 0
	registers := make(map[string]int64)
	for pos >= 0 {
		pos = doInstruction(instructions[pos], pos, registers)
	}
	fmt.Printf("a: %v\n", answer)
}

func doInstructionB(instruction string, pos int, registers map[string] int64, sendqueue []int64, receivequeue []int64, mustCount bool) (int, []int64, []int64) {
	s := strings.Split(instruction, " ")
	switch(s[0]) {
		case "set": return doSet(s[1], s[2], registers, pos), sendqueue, receivequeue
		case "add": return doAdd(s[1], s[2], registers, pos), sendqueue, receivequeue
		case "mul": return doMul(s[1], s[2], registers, pos), sendqueue, receivequeue
		case "mod": return doMod(s[1], s[2], registers, pos), sendqueue, receivequeue
		case "snd": {
				p, q := doSnd(s[1], registers, pos, sendqueue, mustCount)
				return p, q, receivequeue
			}
		case "rcv": {
				p, q := doRcvB(s[1], registers, pos, receivequeue)
				return p, sendqueue, q
			}
		case "jgz": return doJgz(s[1], s[2], registers, pos), sendqueue, receivequeue
		default: fmt.Printf("unknown instruction: %v\n", s); panic("crash and burn");
	}
}

func doInstruction(instruction string, pos int, registers map[string] int64) int {
	s := strings.Split(instruction, " ")
	switch(s[0]) {
		case "set": return doSet(s[1], s[2], registers, pos)
		case "add": return doAdd(s[1], s[2], registers, pos)
		case "mul": return doMul(s[1], s[2], registers, pos)
		case "mod": return doMod(s[1], s[2], registers, pos)
		case "snd": {
				p, _ := doSnd(s[1], registers, pos, []int64{}, false)
				answer = int(getValue(s[1], registers))
				return p
			}
		case "rcv": return doRcv(s[1], registers, pos)
		case "jgz": return doJgz(s[1], s[2], registers, pos)
		default: fmt.Printf("unknown instruction: %v\n", s); panic("crash and burn")
	}
}

func getValue(value string, registers map[string]int64) int64 {
	v, err := strconv.ParseInt(value, 10, 64)
	if err == nil {
		return v
	} else {
		return registers[value]
	}
}

func doSnd(value string, registers map[string]int64, pos int, queue []int64, mustCount bool) (int, []int64) {
	v := getValue(value, registers)
	queue = append(queue, v)
	if mustCount {
		answer++
	}
	return pos + 1, queue

}

func doSet(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] = v
	return pos + 1

}

func doAdd(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] += v
	return pos + 1

}

func doMul(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] *= v
	return pos + 1

}

func doMod(register string, value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	registers[register] %= v
	return pos + 1
}

func doRcvB(register string, registers map[string]int64, pos int, queue []int64) (int, []int64) {
	if len(queue) > 0 {
		registers[register] = queue[0]
		queue = queue[1:]
		return pos + 1, queue
	} else {
		return -1, queue
	}
}

func doRcv(value string, registers map[string]int64, pos int) int {
	v := getValue(value, registers)
	if v == 0 {
		return pos + 1
	} else {
		return -1
	}
}

func doJgz(register string, value string, registers map[string]int64, pos int) int {
	r := getValue(register, registers)
	v := getValue(value, registers)
	if r > 0 {
		return pos + int(v)
	} else {
		return pos + 1
	}
}
