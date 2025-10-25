package main

import "fmt"

func main() {
	var m1 map[string]int = map[string]int{"alice": 1, "bob": 2}

	fmt.Println(m1)
	s1 := []string{"a", "b", "c"}
	e1, ok := m1["aice"]
	fmt.Println(e1, ok)
	fmt.Printf("%q\n", s1)
}
