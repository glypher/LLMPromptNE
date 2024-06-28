FROM python:3.9

WORKDIR /code
 
RUN pip install --no-cache-dir --upgrade fastapi pydantic
 
COPY ./app /code/app
 
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
