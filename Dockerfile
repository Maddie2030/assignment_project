FROM python:3.9-slim
WORKDIR /app
COPY app/ /app
RUN pip install -r /app/requirements.txt
EXPOSE 80
CMD ["python", "app.py"]