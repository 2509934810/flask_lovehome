package web

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

type Case struct {
}
