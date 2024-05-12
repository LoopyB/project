FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apts/lists/*
COPY . /code/
RUN chmod -R a+rwx /code/data/db
EXPOSE 8000
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
ENTRYPOINT ["/wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]


