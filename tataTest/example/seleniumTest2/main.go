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
	opt := []selenium.ServiceOption{}
	selenium.SetDebug(true)
	server, err := selenium.NewChromeDriverService(seleniumPath, port, opt...)
	if err != nil {
		log.Panicln("初始化浏览器失败")
	}
	defer server.Stop()
	caps := selenium.Capabilities{
		"browserName": "chrome",
	}
	client, err := selenium.NewRemote(caps, fmt.Sprintf("http://localhost:%d/wd/hub", port))
	if err != nil {
		log.Panicln(err)
	}
	defer client.Quit()
	client.Get("http://www.baidu.com")
}
