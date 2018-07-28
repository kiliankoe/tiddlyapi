FROM python:3.7-alpine

RUN pip install pipenv

WORKDIR /app

COPY . .

RUN pipenv install

ENTRYPOINT [ "pipenv", "run" ]
CMD [ "python", "main.py" ]
