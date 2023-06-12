FROM python:3.11

ADD database.db .
ADD movies.py .
ADD main.py .

EXPOSE 5000

RUN pip install flask

CMD [ "python", "./main.py"]