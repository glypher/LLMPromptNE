FROM python:3.9

WORKDIR /code
 
RUN pip install --no-cache-dir --upgrade fastapi pydantic 

RUN pip install torch torchdata  --index-url https://download.pytorch.org/whl/cpu

RUN pip install transformers peft
 
COPY ./app /code/app

COPY ./ppo_model_checkpoint /code/app/ppo_model_checkpoint
 
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
