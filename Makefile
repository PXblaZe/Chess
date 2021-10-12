main: main.py
	@echo Compiling main.py ...
	@python3 main.py

test: ts.py
	@echo Compiling ts.py
	@python3 ts.py

utils: utils.py
	@echo Compiling utils.py ...
	@python3 utils.py
