## Backend for an event manager app written in Djando

### Features:
- Event model includes title, description, date, location and organizer
- User registration and authentication with email and password
- REST API in Django Rest Framework
- CRUD operations for the Event model
- Event registration and user notification via email 1 hour before the event using Celery/Redis
- Simple event search based on title and description

### Try it yourself:
```sh
# Do this in your virtual environment
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver

# In another terminal run celery
# Make sure to start Redis before you start celery
celery -A event_manager worker -l info
```