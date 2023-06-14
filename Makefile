export

venv:
	python3 -m venv venv

install: venv
	venv/bin/python && pip3 install -r requirements.txt

test:
	pytest

run: 
	venv/bin/python && python3 manage.py run

all: install run 
