FROM python:3.8.13
WORKDIR /usr/src/nginx
COPY . .

RUN python3 -m pip install -r requirements.txt 
CMD  uvicorn App.app:app
EXPOSE 8000