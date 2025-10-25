package main

import "fmt"

func main() {
    var a [5]int = [5]int {1,2,3,4,5}
    var b []int

    fmt.Println("a size: ", len(a))
    a[2] = 10
    a[3] = 30
    for i,j := range(a) {
        fmt.Println("i: ", i, "j: ", j)
    }

    b = append(b, 10)
    fmt.Println("b size: ", len(b))
    for i := range(b) {
        fmt.Println("i: ", i)
    }
}
