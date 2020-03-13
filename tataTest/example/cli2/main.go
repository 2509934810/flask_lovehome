package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli/v2"
)

func main() {
	app := cli.NewApp()
	app.Flags = []cli.Flag{
		&cli.StringFlag{
			Name:     "lang",
			Value:    "english",
			Usage:    "language for the greeting",
			Required: true,
		},
	}
	app.Action = func(c *cli.Context) error {
		var output string
		if c.String("lang") == "spanish" {
			output = "Hola"
		} else {
			output = "Hello"
		}
		fmt.Println(output)
		return nil
	}
	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
