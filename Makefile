.PHONY: run

run:
	@PYTHONPATH=$PYTHONPATH:$(pwd) python manage.py runserver
