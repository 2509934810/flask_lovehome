package main

import (
	"fmt"
	"log"
	"os"

	"github.com/2509934810/flask_lovehome/tataTest/cases/contro"
	"github.com/urfave/cli/v2"
)

//主入口
func main() {
	app := &cli.App{
		Name:  "greet",
		Usage: "test",
		Action: func(c *cli.Context) error {
			fmt.Println("welcome use tun test framework")
			return nil
		},
	}
	app.Commands = []*cli.Command{
		{
			//执行测试
			Name:  "run",
			Usage: "start your Test",
			Flags: []cli.Flag{
				//选择selenium 类型 默认起本地
				&cli.StringFlag{
					Name:  "selenium",
					Value: "local",
				},
				//并行数量
				&cli.IntFlag{
					Name:    "workers",
					Usage:   "use goroutine",
					Value:   2,
					Aliases: []string{"n"},
				},
				//case 路径
				&cli.StringFlag{
					Name:    "cases",
					Usage:   "Please Input your case Path default is ./",
					Value:   "./",
					Aliases: []string{"c"},
				},
			},
			Action: func(c *cli.Context) error {
				//执行动作
				RunCommand(c)
				return nil
			},
		},
	}
	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}

//
func RunCommand(c *cli.Context) {
	RunConfig()
	workers := c.Int("workers")
	casePath := c.String("cases")
	seleniumType := c.String("selenium")
	contro.Run(workers, casePath, seleniumType)
}

func RunConfig() {
	file := "./" + "message" + ".txt"
	logFile, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0766)
	if err != nil {
		panic(err)
	}
	log.SetOutput(logFile) // 将文件设置为log输出的文件
	log.SetPrefix("[qSkipTool]")
	log.SetFlags(log.LstdFlags | log.Lshortfile | log.LUTC)
}
