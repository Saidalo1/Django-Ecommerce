command mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
	@echo ************  Successfully made migrations and migrated  ************

command admin:
	python3 manage.py createsuperuser