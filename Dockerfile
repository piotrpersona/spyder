FROM python:3.10.0a1-alpine

WORKDIR /man

RUN apk update && apk add --update --no-cache g++ gcc libxslt-dev

COPY requirements.txt .

RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev python-dev libffi-dev openssl-dev make

COPY spyder.py .

ENTRYPOINT [ "/man/spyder.py" ]
