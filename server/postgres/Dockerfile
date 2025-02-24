FROM postgres:17.3

RUN apt update && apt install
## Install pgvector
RUN apt install -y postgresql-17-pgvector

COPY 01-ragdemo.sql /01-ragdemo.sql
COPY doc-5-header /doc-5-header