FROM python:3.6-alpine
RUN pip install flask
RUN pip install requests
COPY . /sentapp
WORKDIR /sentapp
EXPOSE 8088
ENTRYPOINT ["python", "sentapp.py"]
