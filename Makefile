command mig:
	python manage.py makemigrations
	python manage.py migrate
	@echo ************  Successfully made migrations and migrated  ************