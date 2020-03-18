package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{
		Flags: []cli.Flag{
			&cli.StringFlag{
				Name:    "config",
				Aliases: []string{"c"},
				Usage:   "load configure from `FILE`",
			},
			&cli.StringFlag{
				Name:  "start",
				Usage: "start",
			},
		},
		Action: func(c *cli.Context) error {
			fmt.Println("hello")
			return nil
		},
	}
	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
