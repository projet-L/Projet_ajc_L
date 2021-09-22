FROM ubuntu:latest
MAINTAINER Your Name "zuuuuper-meh@crash-test.fr"
RUN apt-get update -y
RUN apt-get install python -y
RUN apt-get install -y python3-pip

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["./app.py"]
