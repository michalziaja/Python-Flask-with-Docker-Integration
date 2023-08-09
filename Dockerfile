FROM python:3.9-alpine

WORKDIR /passgenflask
ADD . /passgenflask

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./app.py
