FROM python:3.8

WORKDIR /app
COPY my_django2.py .
CMD python my_django2.py
