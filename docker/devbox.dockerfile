FROM python:3.7-alpine3.9

WORKDIR /app

COPY cave ./cave
COPY requirements.txt ./requirements.txt
COPY setup.py ./
COPY governor.py ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "governor.py", "run", "--host", "0.0.0.0", "-p", "5000"]
