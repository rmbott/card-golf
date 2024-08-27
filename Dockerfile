#FROM python:3.12-alpine
FROM python:3.12.4-alpine3.20
WORKDIR /card-golf
ENV PATH="/root/.local/bin:$PATH"
RUN apk add --no-cache sqlite curl
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY ./entrypoint.sh /card-golf/
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
