FROM python:3.7.5

COPY ./app app
COPY mongodb_helper mongodb_helper
COPY requirements.txt requirements.txt
COPY .env .env

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t test ./
# docker run -d --name test -p 8000:8000 test