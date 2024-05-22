FROM python:3.10.4

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY addition_app /app/addition_app/
COPY additionproject /app/additionproject/
COPY db.sqlite3 .
COPY manage.py .

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]