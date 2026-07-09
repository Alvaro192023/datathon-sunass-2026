.PHONY: install dev test lint docker clean

install:
	pip install -r requirements.txt

dev:
	pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check --select E9,F63,F7,F82 src tests

docker:
	docker build -t datathon-sunass-2026 .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
