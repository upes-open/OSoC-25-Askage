PYTHON ?= python3

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	FLASK_APP=app.py FLASK_ENV=development $(PYTHON) -m flask run

docker-build:
	docker build -t askage-backend .
