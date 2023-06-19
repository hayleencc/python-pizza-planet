export

hooks:
	cd .git/hooks && ln ../../.github/hooks/pre_commit.py ./pre-commit
	cd .git/hooks && ln ../../.github/hooks/commit_msg.py ./commit-msg
	cd .git/hooks && ln ../../.github/hooks/pre_push.py ./pre-push
	cd .git/hooks && ln ../../.github/hooks/post_checkout.py ./post-checkout


install:
	pip3 install --upgrade pip
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
