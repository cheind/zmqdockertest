ARG DISTNAME=python:3.8-slim
FROM ${DISTNAME} as stage0

WORKDIR /usr/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

FROM stage0 AS producer
EXPOSE 30000
COPY ./src ./src
CMD ["python", "-m", "src.produce"]

FROM stage0 AS consumer
COPY ./src ./src
CMD ["python", "-m", "src.consume"]