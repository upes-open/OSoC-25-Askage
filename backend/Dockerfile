FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV ENV=production

CMD ["gunicorn", "server:app", "--bind", "0.0.0.0:80", "--workers", "1", "--threads", "2"]
