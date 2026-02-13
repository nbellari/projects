package main

import "fmt"

func main() {
	var a []int = []int{1, 2, 4, 5, 6}
	var unknowns []string

	fmt.Println("length of a", len(a))
	fmt.Println(a)
	a = append(a[0:4], a[5:]...)
	fmt.Println("length of a", len(a))
	fmt.Println(a)

	unknowns = append(unknowns, "abc")
	fmt.Println(unknowns)
}
