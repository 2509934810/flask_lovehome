package main

import (
	"log"
	"sync"
)

func main() {
	oneBody := func() {
		log.Println(1)
	}
	ch := make(chan (bool))
	var once sync.Once
	for i := 0; i < 10; i += 1 {
		go func() {
			once.Do(oneBody)
			ch <- true
		}()
	}
	for i := 0; i < 10; i++ {
		<-ch
	}
}
