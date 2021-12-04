package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func readInts(filename, sep string) []int {
	b, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	trimmed := strings.Trim(string(b), "\n ")
	splits := strings.Split(trimmed, sep)

	numbers := make([]int, len(splits))
	for i, numStr := range splits {
		var err error
		numbers[i], err = strconv.Atoi(numStr)
		if err != nil {
			log.Fatal(err)
		}
	}

	return numbers
}

func main() {
	numbers := readInts("input.txt", ",")

	fmt.Printf("Answer 1202: %d\n", runProgram(numbers, 12, 2))

	answer := func() int {
		for noun := 0; noun < 100; noun++ {
			for verb := 0; verb < 100; verb++ {
				out := runProgram(numbers, noun, verb)
				if out == 19690720 {
					return 100*noun + verb
				}
			}
		}
		return 0
	}()

	fmt.Printf("Answer noun and verb: %d\n", answer)
}

func runProgram(nums []int, a, b int) int {
	array := append([]int{}, nums...)
	array[1] = a
	array[2] = b
	i := 0
	for {
		opcode := array[i]
		switch opcode {
		case 1:
			array[array[i+3]] = array[array[i+1]] + array[array[i+2]]
		case 2:
			array[array[i+3]] = array[array[i+1]] * array[array[i+2]]
		case 99:
			return array[0]
		default:
			log.Fatalf("unexpected opcode: %d", opcode)
		}
		i += 4
	}
}

type Foo struct {
	A int
	B string
}

var (
	s = Foo{A: 3, B: "hello"}
)
