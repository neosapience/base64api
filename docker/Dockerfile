FROM python:3.8.3-alpine3.12
RUN pip install flask gunicorn pyjsend pytest \
    && rm -rf /root/.cache/pip

WORKDIR /opt/code
COPY ./app .

ENV PYTHONPATH=/opt/code
ENTRYPOINT ["./docker-entrypoint.sh"]