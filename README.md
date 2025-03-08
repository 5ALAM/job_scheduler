# Job Scheduler Project

## Installation
1. Clone the repository:
git clone https://github.com/5ALAM/job_scheduler.git


2. Navigate into the project:
cd job-scheduler


3. Set up a virtual environment:
python -m venv venv venv\Scripts\activate # For Windows


4. Install dependencies:
pip install -r requirements.txt


5. Configure your **database** in `settings.py`:
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'jobscheduler_db', 'USER': 'your_db_user', 'PASSWORD': 'your_password', 'HOST': 'localhost', 'PORT': '5432', } }


6. Apply migrations:
python manage.py makemigrations python manage.py migrate


7. Run the server:
python manage.py runserver
