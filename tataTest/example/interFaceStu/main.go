package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"gopkg.in/yaml.v2"
)

type StepBody struct {
	CheckTpye string   `yaml:"checktype"`
	Timeout   int8     `yaml:"timeout"`
	CheckBody []string `yaml:"checkbody"`
}

type WebCase struct {
	Name  string     `yaml:"name"`
	Url   string     `yaml:"url"`
	Check []StepBody `yaml:"check"`
}

//Case interFace
type Case interface {
	Check()
	Invoke()
}

func Check() {

}

func Invoke() {

}

func main() {
	file, err := ioutil.ReadFile("./test.yaml")
	if err != nil {
		log.Println(err)
	}
	log.Println(file)
	caseBody := []WebCase{}
	err = yaml.Unmarshal(file, &caseBody)
	if err != nil {
		log.Println(err)
	}
	fmt.Println(caseBody)
}
