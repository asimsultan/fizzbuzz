FROM python:3.9

ENV SRC_DIR C:\Users\asims\Downloads\Deep Learning\EDA\containerize-python-server

COPY src/* ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONBUFFERED=1

CMD ["python", "python_server.py"]