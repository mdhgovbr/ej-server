FROM python:3.5

ENV PYTHONUNBUFFERED 1


WORKDIR /app

# ext-apps need to be pulled here too, or live-reloading won't work
COPY ./requirements /app/requirements
COPY ./ext-apps /app/ext-apps
RUN pip install -r /app/requirements/test.txt

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/dev/django/test.sh /test.sh
RUN sed -i 's/\r//' /test.sh
RUN chmod +x /test.sh

COPY ./compose/local/django/runserver.sh /runserver.sh
RUN sed -i 's/\r//' /runserver.sh
RUN chmod +x /runserver.sh

COPY . /app

ENTRYPOINT ["/entrypoint.sh"]
