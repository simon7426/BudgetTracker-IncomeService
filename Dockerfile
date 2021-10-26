FROM python:3.8.12-slim-buster

ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 8000

COPY . /app
CMD ["gunicorn", "budget_tracker_income_service.wsgi", "--workers","4","--bind","0.0.0.0:8000"]