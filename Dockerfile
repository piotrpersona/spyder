FROM python:3.9-slim-buster

WORKDIR /man

RUN apt update && apt install libxml2-dev libxslt1-dev python-dev

COPY requirements.txt .

RUN pip3 install -U pip Cython && pip3 install -r requirements.txt

COPY spyder.py .

ENTRYPOINT [ "/man/spyder.py" ]
