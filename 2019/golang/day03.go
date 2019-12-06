package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

type point struct {
    x int
    y int
}

func getRoute(directions string) []point {
    x, y := 0, 0
    route := make([]point, 0)
    for _, move := range strings.Split(directions, ",") {
        direction, distance := byte(0), 0
        fmt.Sscanf(move, "%c%d", &direction, &distance)
        for i := 0; i < distance; i++ {
            switch direction {
            case 'U':
                y++
            case 'R':
                x++
            case 'D':
                y--
            case 'L':
                x--
            }
            route = append(route, point{x, y})
        }
    }
    return route
}

func getIntersect(r1 []point, r2 []point) map[point]int {
    m := make(map[point]int)
    for _, p := range r2 {
        m[p]++
    }
    intersect := make(map[point]int)
    for _, p := range r1 {
        if m[p] > 0 {
            intersect[p]++
        }
    }
    return intersect
}

func main() {

    file, _ := os.Open("../input/day3.input")
    defer file.Close()
    scanner := bufio.NewScanner(file)
    scanner.Scan()
    r1 := getRoute(scanner.Text())
    scanner.Scan()
    r2 := getRoute(scanner.Text())
    intersect := getIntersect(r1, r2)

    closest := 999999999
    for k, _ := range intersect {
        x, y := k.x, k.y
        if x < 0 {
            x *= -1
        }
        if y < 0 {
            y *= -1
        }
        if x+y < closest {
            closest = x + y
        }
    }
    fmt.Printf("answer a: %v\n", closest)

    closest = 999999999
    d1, d2 := 0, 0
    for k, _ := range intersect {
        for i := 0; i < len(r1); i++ {
            if r1[i] == k {
                d1 = i
            }
        }
        for i := 0; i < len(r2); i++ {
            if r2[i] == k {
                d2 = i
            }
        }
        if d1+d2 < closest {
            closest = d1 + d2
        }
    }
    fmt.Printf("answer a: %v\n", 2+closest)
}
