FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt /code

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code

EXPOSE 3100

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3100","--reload"]
