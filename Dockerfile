FROM python:3.10
WORKDIR /app
ARG APP_VERSION
COPY app/${APP_VERSION}/app.py /app/
RUN pip install flask
CMD ["python", "app.py"]
