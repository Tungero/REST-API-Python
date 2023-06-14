# in cmd write:
# docker build -t python-rest-api .
# docker run -p 5000:5000 python-rest-api

FROM python:3.11

ADD database.db .
ADD movies.py .
ADD main.py .

EXPOSE 5000

RUN pip install flask

CMD [ "python", "./main.py"]
