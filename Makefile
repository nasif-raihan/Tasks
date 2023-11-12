.PHONE:
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

.PHONE:
venv:
	poetry install
	poetry update

.PHONE:
run-local:
	python3 manage.py runserver

.PHONE:
run-docker:
	docker build -t tasks .
	docker run --rm -p 8000:8000 tasks