FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# For Alpine
# RUN apk add --no-cache --virtual .build-deps \
#     gcc musl-dev libffi-dev openssl-dev

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# For Alpine
# RUN apk del .build-deps

COPY ./app /code/app

CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]