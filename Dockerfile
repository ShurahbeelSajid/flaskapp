FROM python:3.8-alpine

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]


