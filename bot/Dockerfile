from python:3.10

WORKDIR /usr/src/app

COPY .env .env
COPY requirements.txt requirements.txt
COPY sheenbot.py sheenbot.py 
RUN pip3 install -r requirements.txt

CMD python sheenbot.py
