#FROM python:3.12-alpine
FROM python:3.12.4-alpine3.20

# set the working directory
WORKDIR /app

#RUN apk add --no-cache python3 py3-pip
RUN apk add curl
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY ./pyproject.toml /app
RUN poetry install
RUN poetry run fastapi dev main
#RUN export PATH="/root/.local/bin:$PATH"

# # install dependencies
# COPY ./requirements.txt /app
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# # copy the scripts to the folder
# COPY . /app

# # start the server
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
