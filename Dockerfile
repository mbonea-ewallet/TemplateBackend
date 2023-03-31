FROM python:3.8.13
WORKDIR /usr/src/nginx
COPY . .

RUN python3 -m pip install -r requirements.txt 
CMD  gunicorn main:app --workers 4   --host 0.0.0.0
EXPOSE 8000