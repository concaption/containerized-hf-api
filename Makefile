setup:
	chmod +x ./setup.sh &&\
		./setup.sh
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	python -m pytest -vv --cov=main test_*.py &&\
	python -m pytest --nbval notebook.ipynb
format:
	black *.py
lint:
	pylint --disable=R,C *.py
refactor: format lint
deploy:
	# deploy goes here
run:
	uvicorn webapp.main:app --reload --host 0.0.0.0 --port 8000 --log-level debug
run-docker:
	docker-compose up --build
all: install lint test format deploy
