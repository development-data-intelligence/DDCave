FROM python:3.7-alpine3.9

COPY ./cave /cave
COPY ./requirements.txt /cave/requirements.txt

WORKDIR /cave

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
