FROM ubuntu:latest
MAINTAINER Dani Simonyan
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["vxsoft_task.py"]
