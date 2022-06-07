FROM python:3.9.13-alpine3.16
LABEL maintainer="icalboardgold@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    mkdir -p staticfiles && \
    mkdir -p mediafiles && \
    chmod -R 755 staticfiles && \
    chmod -R 755 mediafiles && \
    chmod +x entrypoint.sh

ENV PATH="/opt/venv/bin:$PATH"

CMD ["/app/entrypoint.sh"]

