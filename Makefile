init:
	docker-compose -f docker-compose-env.yaml up -d

run:
	echo "hello"

help:
	@echo "|---------------------------------------|"
	@echo "|---------------flask home--------------|"
	@echo "|                                       |"
	@echo "|---------------------------------------|"