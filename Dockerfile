FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip
COPY task_app/app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["vxsoft_task.py"]