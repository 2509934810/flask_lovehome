package main

import (
	"fmt"
	"log"

	"github.com/tebeka/selenium"
	// "github.com/tebeka/selenium/chrome"
)

func main(){
	selenium.SetDebug(true)
	server, err := selenium.NewChromeDriverService(`/usr/local/bin/chromedriver`, 8081)
	if err != nil{
		log.Println(err)
	}
	defer server.Stop()
	caps := selenium.Capabilities{"browserName": "chrome"}
	wd, err := selenium.NewRemote(caps, fmt.Sprintf("http://localhost:%d/wd/hub", 8081))
	if err != nil{
		log.Println(err)
	}
	defer wd.Quit()
	wd.Get("http://www.baidu.com")
	wd.FindElement(selenium.ByCSSSelector, "#qrcode > div > div.qrcode-img")
	input, err := wd.FindElement(selenium.ByCSSSelector, "#kw")
	if err != nil{
		log.Println(err)
	}
	input.SendKeys("鸡蛋")
	click, err := wd.FindElement(selenium.ByCSSSelector, "#su")
	if err != nil{
		log.Println(err)
	}
	click.Click()
	wd.Get("https://www.taobao.com")
}
