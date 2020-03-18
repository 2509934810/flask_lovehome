package main

import (
	"log"
	"sync"
	"time"
)

type BasePoll struct {
	size   int
	job    func()
	jobNum int
}

type Poll BasePoll

func workers(wd *sync.WaitGroup, ch *chan (int), job func()) {
	job()
	c := <-*ch
	log.Println(c)
	wd.Done()
}

func (poll Poll) Run() {
	wd := sync.WaitGroup{}
	wd.Add(poll.jobNum)
	c := make(chan (int), poll.size)
	for poll.jobNum > 0 {
		c <- poll.jobNum
		go workers(&wd, &c, poll.job)
		poll.jobNum--
	}
	wd.Wait()
}

func worker() {
	time.Sleep(time.Second * 1)
	log.Println(1)
}

func main() {
	poll := Poll{3, worker, 100}
	poll.Run()
}
