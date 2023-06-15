export

install: 
	pip3 install -r requirements.txt

test:
	pytest

run:
	python3 manage.py run

all: install run
