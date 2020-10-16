FROM python:3.9-slim-buster

WORKDIR /man

RUN apt update && apt install -y libxml2-dev libxslt-dev python3-dev

COPY requirements.txt .

RUN pip3 install -U pip Cython && pip3 install -r requirements.txt

COPY spyder.py .

ENTRYPOINT [ "/man/spyder.py" ]
