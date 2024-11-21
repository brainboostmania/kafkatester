FROM python:3.13

COPY requirements.txt /usr/app/

WORKDIR /usr/app/
RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run", "--debug", "--host", "0.0.0.0"]