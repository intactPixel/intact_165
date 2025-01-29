package main

import (
	"fmt"
	"math/rand"
)

func main() {
	a := []int{}
	for i := 0; i < 20; i++ {
		a = append(a, rand.Intn(1000)+100)
	}
	fmt.Println("unsorted array:", a)
	bubbleSort(a)
	fmt.Println("sorted array:", a)
	fmt.Println(a)

}

func bubbleSort(array []int) {
	fmt.Println("buble sort start:")
	for i := 0; i < len(array)-1; i++ {
		swapped := false
		for j := 0; j < len(array)-1-i; j++ {
			if array[j] > array[j+1] {
				array[j], array[j+1] = array[j+1], array[j]
				swapped = true
			}
		}
		if !swapped {
			fmt.Println("buble sort finish")
			break
		}
	}
}
