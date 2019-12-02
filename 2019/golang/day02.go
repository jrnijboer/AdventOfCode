package main
import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func main() {
    for noun := 0; noun < 100; noun++ {
        for verb := 0; verb < 100; verb++ {
            values, _ := ioutil.ReadFile("../input/day2.input")
            input := []int{}
            for _, s := range strings.Split(string(values), ",") {
                i, _ := strconv.Atoi(s)
                input = append(input, i)
            }
            ip, opcode := 0, input[0]
            input[1], input[2] = noun, verb
            for opcode != 99 {
                if opcode == 1 {
                    input[input[ip + 3]] = input[input[ip + 1]] + input[input[ip + 2]]
                }
                if opcode == 2 {
                    input[input[ip + 3]] = input[input[ip + 1]] * input[input[ip + 2]]
                }
                ip += 4
                opcode = input[ip]
            }
            if noun == 12 && verb == 2 {
                fmt.Printf("answer a: %v\n", input[0])
            }
            if input[0] == 19690720 {
                fmt.Printf("answer b: %v\n", 100 * noun + verb)
            }
        }
    }
}
