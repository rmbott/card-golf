#FROM python:3.12-alpine
FROM python:3.12.4-alpine3.20
WORKDIR /app
ENV PATH="/root/.local/bin:$PATH"
RUN apk add curl
RUN curl -sSL https://install.python-poetry.org | python3 -
# COPY . /app
# RUN /root/.local/bin/poetry install
COPY ./entrypoint.sh /app/
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
