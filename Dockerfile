FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN apk add --no-cache gcc musl-dev linux-headers && \
	pip install --trusted-host pypi.python.org -r requirements.txt && \
	apk del gcc musl-dev linux-headers

#EXPOSE 5000

CMD ["python","app.py"]
