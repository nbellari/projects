package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var total, nInts, nFloats int
	var unknowns []string

	if len(os.Args) == 1 {
		fmt.Println("No command line arguments given!")
		return
	}

	for _, val := range os.Args[1:] {
		total += 1
		_, err := strconv.Atoi(val)
		if err == nil {
			nInts += 1
			continue
		}

		_, err = strconv.ParseFloat(val, 64)
		if err == nil {
			nFloats += 1
			continue
		}

		unknowns = append(unknowns, val)
	}

	fmt.Printf("Total arguments: %d, Ints: %d, Floats: %d\n", total, nInts, nFloats)
	if len(unknowns) > 0 {
		fmt.Print("Unknowns: ", unknowns, "\n")
	}
}
