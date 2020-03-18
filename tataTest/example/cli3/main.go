package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{
		Name:  "test",
		Usage: "a",
		Commands: []*cli.Command{
			{
				Name:    "compelete",
				Aliases: []string{"c"},
				Usage:   "compelete",
				Action: func(c *cli.Context) error {
					fmt.Println("ello")
					return nil
				},
			},
			{
				Name:    "add",
				Usage:   "add command to line",
				Aliases: []string{"a"},
				Action: func(c *cli.Context) error {
					fmt.Println("add command")
					return nil
				},
			},
			{
				Name:    "template",
				Usage:   "create a template",
				Aliases: []string{"t"},
				Subcommands: []*cli.Command{
					{
						Name:  "add",
						Usage: "add tem",
						Action: func(c *cli.Context) error {
							fmt.Println("add tem")
							return nil
						},
					},
				},
			},
		},
	}
	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
