run: main.py
	@echo Compiling main.py ...
	@python3 -O main.py

debug: main.py
	@echo checking typing ...
	@mypy main.py