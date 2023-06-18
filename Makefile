export

install: 
	pip3 install -r requirements.txt

test:
	pytest

run:
	python3 manage.py run

seed:
	python3 manage.py seed

drop-tables:
	python3 manage.py drop

all: install run
