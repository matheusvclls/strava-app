 
FROM python:3.9


WORKDIR /code

 
COPY ./requirements.txt /code/requirements.txt

COPY ./.env /code/.env
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

 
COPY ./src /code/src

CMD ["uvicorn", "src.main.config.http_server_configs:app", "--host", "0.0.0.0", "--port", "80"]
