# Mini Event Management System API

## Tech Stack
- Python + Django + Django REST Framework
- SQLite DB
- Swagger (drf-yasg)
- Unit tests (DRF test client)

## Setup Instructions
**Clone the project**  

1. git clone https://github.com/pr40934/Omnify-Sr-Python-dev.git
2. cd Omnify-Sr-Python-dev
3. python -m venv env

# Windows
env\Scripts\activate

# macOS/Linux
source env/bin/activate
 
4. pip install -r requirements.txt

5. python manage.py makemigrations
   
6. python manage.py migrate

7. python manage.py runserver

**8. Swagger UI**
Open http://127.0.0.1:8000/swagger/ in your browser

 **API Endpoints**
| Method | Endpoint                  | Description              |
| ------ | ------------------------- | ------------------------ |
| POST   | `/events/`                | Create an event          |
| GET    | `/events/`                | List all events          |
| POST   | `/events/<id>/register/`  | Register an attendee     |
| GET    | `/events/<id>/attendees/` | List attendees for event |


**Run Tests**
python manage.py test events


