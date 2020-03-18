package contro

import (
	"fmt"
	"io/ioutil"
	"log"

	"github.com/2509934810/flask_lovehome/tataTest/cases/web"
	"github.com/tebeka/selenium"
	"gopkg.in/yaml.v2"
)

type Webcase web.WebCase

func Run(workers int, casePath string, seleniumType string) {
	caseStr := []web.WebCase{}
	parse(casePath, &caseStr)
	// collection, ctx := utils.MongoDb()
	pool := Pool{workers, RunCase, len(caseStr), caseStr}
	pool.Run()
}

func RunCase(caseBody web.WebCase) {
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
		log.Println(err)
	}
	defer client.Quit()
	client.Get(caseBody.Url)
	web.RunStep(client, caseBody)
}

func parse(casePath string, dataStruct *[]web.WebCase) {
	file, err := ioutil.ReadFile(casePath)
	if err != nil {
		log.Println(err)
	}
	yaml.Unmarshal(file, dataStruct)
}
