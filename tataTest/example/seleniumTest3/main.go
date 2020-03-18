package main

import (
	"fmt"
	"log"

	"github.com/tebeka/selenium"
)

func main() {
	const (
		seleniumPath = `/usr/local/bin/chromedriver`
		port         = 8080
	)
	opts := []selenium.ServiceOption{}
	// selenium.SetDebug(true)
	server, err := selenium.NewChromeDriverService(seleniumPath, port, opts...)
	if err != nil {
		log.Println(err)
	}
	defer server.Stop()
	caps := selenium.Capabilities{}
	client, err := selenium.NewRemote(caps, fmt.Sprintf("http://localhost:%d/wd/hub", port))
	if err != nil {
		log.Panic(err)
	}
	defer client.Quit()
	client.Wait(selenium.Condition(client))
	selenium.WebDriver.Wait(client, selenium.Condition)
}
