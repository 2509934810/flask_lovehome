CaseFile = test.yaml
Workers = 1

mongod:
	mongod --dbpath /tmp/

run:
	bin/tun run -c $(CaseFile) --workers $(Workers)

show:
	ls

help:
	@echo "===============A common Makefilefor ==============" 
	@echo "Copyright (C) 2020 lovehome  test framework!" 
	@echo "The following targets aresupport:" 
	@echo 
	@echo " run              - make run test.yaml" 
	@echo " help             - print help information" 
	@echo 
	@echo "================   Version1.0  ====================" 