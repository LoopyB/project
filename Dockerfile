FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod -R a+rwx /code/data/db
WORKDIR /code
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

