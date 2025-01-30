package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// Устанавливаем заголовок Content-Type
	w.Header().Set("Content-Type", "text/html; charset=utf-8")

	// Открываем HTML-файл
	http.ServeFile(w, r, "index.html")
}

func main() {
	//a := []int{}
	//for i := 0; i < 20; i++ {
	//	a = append(a, rand.Intn(1000)+100)
	//}
	//fmt.Println("unsorted array:\n", a)
	//bubbleSort(a)
	//fmt.Println("sorted array:", a)
	//fmt.Println(a)
	//
	//for _, i := range a {
	//	fmt.Printf("%d ", i)
	//}
	// handler функция для обработки HTTP-запросов

	// Устанавливаем обработчик для корневого маршрута
	http.HandleFunc("/", handler)

	// Запускаем сервер на порту 8080
	log.Println("Сервер запущен на http://localhost:8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal("Ошибка при запуске сервера:", err)
	}
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
