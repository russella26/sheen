FROM python:3.7

WORKDIR /usr/src/app

COPY aitextgen.tokenizer.json aitextgen.tokenizer.json
COPY gentest.py gentest.py
COPY requirements.txt requirements.txt
COPY sheenserver.py sheenserver.py
COPY trained_model trained_model

RUN pip install -r requirements.txt

EXPOSE 5000

CMD export FLASK_APP=sheenserver && flask run --host=0.0.0.0
