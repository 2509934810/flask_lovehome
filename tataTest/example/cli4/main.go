package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{}
	app.UseShortOptionHandling = true
	app.Action = func(c *cli.Context) error {
		fmt.Println("start your test")
		return nil
	}
	// app.Flags = []cli.Flag{
	// 	&cli.StringFlag{
	// 		Name:    "config",
	// 		Usage:   "select your config Path",
	// 		Aliases: []string{"c"},
	// 		Value:   "./",
	// 	},
	// }
	app.Commands = []*cli.Command{
		{
			Name:  "run",
			Usage: "create your test",
			Flags: []cli.Flag{
				&cli.StringFlag{
					Name:  "case",
					Usage: "change case path",
				},
				&cli.StringFlag{
					Name:  "selenium",
					Usage: "change your selenium uri",
				},
				&cli.StringFlag{
					Name:  "config",
					Usage: "input your config file",
					Value: "./",
				},
			},
			Action: func(c *cli.Context) error {
				fmt.Println(c.String("case"))
				fmt.Println(c.String("selenium"))
				fmt.Println(c.String("config"))
				return nil
			},
		},
	}
	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
