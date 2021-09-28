# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update 
#    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install psycopg2-binary

# copy project
COPY ./worker .
#Primer Param del local segundo img
# run entrypoint.sh
#ENTRYPOINT ["/usr/src/worker/entrypoint.sh"]
RUN pwd
RUN ls

CMD ["python","manage.py","runserver","0.0.0.0:8000"]