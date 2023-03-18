FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir numba==0.48

COPY . .

CMD ["/bin/sh", "-c", "\
  export TF_CPP_MIN_LOG_LEVEL=3; \
  export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python; \
  python init.py"]