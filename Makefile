.PHONY: tests lint type-check all

tests:
	@echo Running tests...
	python -m unittest discover -s tests

lint:
	@echo Running linter...
	flake8 . --exclude=venv

type-check:
	@echo Running type checker...
	mypy . --exclude=venv

all: tests lint type-check
	@echo Completed all tasks.