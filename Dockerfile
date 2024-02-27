FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python bookstore.py

