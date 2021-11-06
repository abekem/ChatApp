FROM python:3.9
ADD . /chatapp
WORKDIR /chatapp
RUN pip install -r requirements.txt
CMD ["python", "manage.py"]
