FROM python:3.8.13
WORKDIR /usr/src/nginx
COPY . .

RUN python3 -m pip install -r requirements.txt 
CMD  uvicorn App.app:app --host 0.0.0.0 --workers 10
EXPOSE 8000