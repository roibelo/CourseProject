FROM python:3-alpine
COPY Backend/rest_app.py /
COPY Backend/db_connector.py /
COPY Backend/backend_testing.py /
copy Backend/clean_environment.py /
COPY Backend/requirements.txt /
RUN pip install -r requirements.txt
CMD ["python","./rest_app.py"]