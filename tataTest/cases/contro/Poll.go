package contro

import (
	"log"
	"sync"

	"github.com/2509934810/flask_lovehome/tataTest/cases/web"
)

type WebCase web.WebCase

type BasePool struct {
	Size     int
	Job      func(web.WebCase)
	JobNum   int
	CaseBody []web.WebCase
}

type Pool BasePool

func worker(wd *sync.WaitGroup, caseBody []web.WebCase, ch *chan (int), ch2 *chan (int), job func(web.WebCase)) {
	jobId := <-*ch2
	// log.Println(jobId)
	job(caseBody[jobId-1])
	<-*ch
	(*wd).Done()
}

func (pool Pool) Run() {
	var wd sync.WaitGroup
	wd.Add(pool.JobNum)
	log.Printf("job 数量: %d", pool.JobNum)
	//ch通道控制并发数量
	ch := make(chan (int), pool.Size)
	//来控制并发数量的函数参数
	ch2 := make(chan (int), pool.Size)
	for pool.JobNum > 0 {
		ch <- pool.JobNum
		ch2 <- pool.JobNum
		go worker(&wd, pool.CaseBody, &ch, &ch2, pool.Job)
		pool.JobNum--
	}
	wd.Wait()
}
