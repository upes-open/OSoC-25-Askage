PYTHON ?= python3

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) backend/server.py

docker-build:
	docker build --no-cache -t askage-backend .
