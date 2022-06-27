FROM python:3.8.13-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]