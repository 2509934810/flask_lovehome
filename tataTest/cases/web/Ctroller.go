package web

// import (
// 	"fmt"
// 	"log"

// 	"github.com/tebeka/selenium"
// )

// type Webcase WebCase

// func CreateClient() selenium.WebDriver {
// 	const (
// 		seleniumPath = `/usr/local/bin/chromedriver`
// 		port         = 8080
// 	)
// 	opts := []selenium.ServiceOption{}
// 	selenium.SetDebug(true)
// 	server, err := selenium.NewChromeDriverService(seleniumPath, port, opts...)
// 	if err != nil {
// 		log.Println(err)
// 	}
// 	defer server.Stop()
// 	caps := selenium.Capabilities{}
// 	client, err := selenium.NewRemote(caps, fmt.Sprintf("http://localhost:%d/wd/hub", port))
// 	if err != nil {
// 		log.Println(err)
// 	}
// 	defer client.Quit()
// 	client.Get("https://www.baidu.com")
// 	return client
// }

// func (webcase Webcase) CheckCase(client selenium.WebDriver) {
// 	client.Get("https://www.baidu.com")
// 	for _, step := range webcase.Check {
// 		switch step.CheckTpye {
// 		case "find":
// 			func() {
// 				for _, checkBody := range step.CheckBody {
// 					client.FindElement(selenium.ByCSSSelector, checkBody)
// 				}
// 			}()
// 		default:
// 			log.Println("error")
// 		}
// 	}
// }

// func (webcase Webcase) InvokeCase() {
// 	fmt.Println("start Invoke")
// }
