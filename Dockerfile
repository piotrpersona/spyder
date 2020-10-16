FROM python:3.10.0a1-alpine

WORKDIR /man

RUN apk update && apk add --update --no-cache g++ gcc libxslt-dev

COPY requirements.txt .

RUN pip3 install -U pip && pip3 install -r requirements.txt

COPY spyder.py .

ENTRYPOINT [ "/man/spyder.py" ]
