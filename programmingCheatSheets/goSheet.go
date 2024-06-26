package main

import (
	"errors"
	"fmt"
)

func main() {
	demonstrateDataTypes()
	demonstrateControlStructures()
	demonstrateFunctions()
	demonstrateStructsAndInterfaces()
	demonstrateErrorHandling()
	demonstrateConcurrency()
}

func demonstrateDataTypes() {
	var i int = 42
	var f float64 = 3.1415
	var b bool = true
	var s string = "GoLang"
	var r rune = 'G'

	fmt.Println("Data Types:")
	fmt.Println(i, f, b, s, r)
	fmt.Println()
}

func demonstrateControlStructures() {
	i := 5
	fmt.Println("Control Structures:")

	if i > 10 {
		fmt.Println("Greater than 10")
	} else {
		fmt.Println("Less than or equal to 10")
	}

	switch i {
	case 1:
		fmt.Println("One")
	default:
		fmt.Println("Not one")
	}

	for j := 0; j < 5; j++ {
		fmt.Println(j)
	}

	k := 0
	for k < 5 {
		fmt.Println(k)
		k++
	}

	nums := []int{1, 2, 3}
	for index, value := range nums {
		fmt.Println(index, value)
	}
	fmt.Println()
}

func demonstrateFunctions() {
	fmt.Println("Functions:")
	fmt.Println(add(42, 13))
	a, b := swap("hello", "world")
	fmt.Println(a, b)
	fmt.Println()
}

func add(x int, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

type Person struct {
	Name string
	Age  int
}

func (p Person) Greet() {
	fmt.Println("Hi, my name is", p.Name)
}

type Greeter interface {
	Greet()
}

func demonstrateStructsAndInterfaces() {
	fmt.Println("Structs and Interfaces:")
	p := Person{Name: "John", Age: 30}
	p.Greet()
	fmt.Println()
}

func demonstrateErrorHandling() {
	fmt.Println("Error Handling:")
	result, err := div(5, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Result:", result)
	}
	fmt.Println()
}

func div(x, y int) (int, error) {
	if y == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return x / y, nil
}

func demonstrateConcurrency() {
	fmt.Println("Concurrency:")
	// Goroutine for concurrent function execution
	go func(msg string) {
		fmt.Println(msg)
	}("Going")

	// Channels for communication between goroutines
	messages := make(chan string)
	go func() { messages <- "ping" }()
	msg := <-messages
	fmt.Println(msg)
	fmt.Println()
}
