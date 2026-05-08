# =========================
# BASE
# =========================
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /code

RUN useradd -m appuser && chown -R appuser /code

FROM base AS builder

COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# =========================
# PROD
# =========================
FROM base AS prod

COPY requirements.txt .

COPY --from=builder /wheels /wheels

RUN pip install --no-cache-dir /wheels/* \
 && rm -rf /wheels

COPY ./app /code/app

USER appuser

EXPOSE 80

CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]

# =========================
# DEV
# =========================
FROM base AS dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
 && pip install uvicorn

COPY ./app /code/app

USER appuser

EXPOSE 80

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]