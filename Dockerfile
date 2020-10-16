FROM python:3.9-slim-buster

WORKDIR /man

COPY requirements.txt .

RUN pip3 install -U pip && pip3 install -r requirements.txt

COPY spyder.py .

ENTRYPOINT [ "/man/spyder.py" ]
