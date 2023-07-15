FROM python:3-alpine
COPY rest_app.py /
COPY db_connector.py /
COPY backend_testing.py /
COPY clean_environment.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD ["python","./rest_app.py"]