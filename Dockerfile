FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirement.txt
ENTRYPOINT ["python", "dictonary-api"]
