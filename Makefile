setup:
	pip install -r requirements.txt

run:
	python manage.py runserver

check:
	ruff check .

format:
	ruff format .

docker-up:
	docker compose up --build

docker-down:
	docker compose down

logs:
	docker compose logs -f