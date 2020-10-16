FROM python:3.10.0a1-alpine

WORKDIR /man

RUN apk update && apk add --update --no-cache g++ python3-dev \
        libxml2 libxml2-dev \
    && apk add libxslt-dev

COPY requirements.txt .

RUN pip3 install -U pip && pip3 install -r requirements.txt

COPY spyder.py .

ENTRYPOINT [ "/man/spyder.py" ]
