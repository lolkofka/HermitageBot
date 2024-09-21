FROM python:3.12.6

WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./assets ./assets
COPY ./src ./src

ENV PYTHONPATH=/usr/app/src
ENV TZ="Europe/Moscow"

CMD [ "python", "src/main.py" ]