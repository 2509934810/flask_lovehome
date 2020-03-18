package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	// var wd sync.WaitGroup
	// wd.Add(100)
	var lock sync.Mutex
	var num int
	for i := 0; i < 1000; i++ {
		go func() {
			lock.Lock()
			defer lock.Unlock()
			// log.Panicln(a)
			num++
			fmt.Println(num)
			// wd.Done()
		}()
	}
	time.Sleep(time.Second)
	fmt.Printf("the num is :%d\n", num)
}
