package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Card struct {
	Rows [10][]int
}

func Day04() {
	file, _ := os.Open("../input/day04.input")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var rng []int
	game := make(map[int]Card)
	maxCardId := 0

	// read rows for all cards
	for scanner.Scan() {
		if len(rng) == 0 {
			numbers := strings.Split(scanner.Text(), ",")
			for _, s := range numbers {
				number, _ := strconv.Atoi(s)
				rng = append(rng, number)
			}
		} else {
			line := scanner.Text()
			if line == "" {
				card := Card{}
				for i := 0; i < 5; i++ {
					scanner.Scan()
					var row []int
					line = scanner.Text()
					numbers := strings.Fields(line)
					for _, s := range numbers {
						number, _ := strconv.Atoi(s)
						row = append(row, number)
					}
					card.Rows[i] = row
				}
				game[maxCardId] = card
				maxCardId++
			}
		}
	}

	// create columns for all cards
	for i := 0; i < maxCardId; i++ {
		card := game[i]
		for j := 5; j < 10; j++ {
			var column []int
			for k := 0; k < 5; k++ {
				column = append(column, card.Rows[k][j-5])
			}
			card.Rows[j] = column
		}
		game[i] = card
	}

	// start the game, call the numbers from the RNG
	for _, number := range rng {
		bingoCards := make(map[int]int)
		for cardId, card := range game {
			hasBingo := false
			for rowId, row := range card.Rows {
				foundNumber := -1
				for pos, n := range row {
					if n == number {
						foundNumber = pos
					}
				}
				if foundNumber >= 0 {
					// do weird stuff to remove foundNumnber from row
					// apparently this is the way: https://stackoverflow.com/a/37335777
					row[foundNumber] = row[len(row)-1]
					row = row[:len(row)-1]
					card.Rows[rowId] = row
				}
				if len(row) == 0 {
					hasBingo = true
					bingoCards[cardId]++
				}
			}

			// card has bingo, calculate remaining numbers
			if hasBingo {
				//first find the unique remaining numbers
				remaining := make(map[int]int)
				for _, row := range card.Rows {
					for _, n := range row {
						remaining[n]++
					}
				}

				//now sum the remaining numbers
				sumRemaining := 0
				for n, _ := range remaining {
					sumRemaining += n
				}
				if len(game) == 100 {
					fmt.Println("Answer A:", number*sumRemaining)
				}
				if len(game) == 1 {
					fmt.Println("Answer B:", number*sumRemaining)
				}
			}
			game[cardId] = card
		}

		//find completed cards and remove from game
		for key := range bingoCards {
			delete(game, key)
		}
	}
}
