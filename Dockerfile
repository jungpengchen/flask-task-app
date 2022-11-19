FROM python:3.7-slim AS builder
WORKDIR /app/src
COPY requirement.txt /app/requirement.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirement.txt

FROM builder as runner
ENV FLASK_APP=server.py
ENV FLASK_DEBUG=0
COPY src /app/src
CMD flask run --with-threads