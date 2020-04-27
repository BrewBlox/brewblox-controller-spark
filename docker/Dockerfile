FROM python:3.7 as base

COPY ./dist /app/dist
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install wheel \
    && pip3 wheel --wheel-dir=/wheeley --extra-index-url=https://www.piwheels.org/simple -r /app/requirements.txt \
    && pip3 wheel --wheel-dir=/wheeley --find-links=/wheeley --no-index /app/dist/*

FROM python:3.7-slim
EXPOSE 5000
WORKDIR /app

ARG service_info=UNKNOWN
ENV SERVICE_INFO=${service_info}

COPY --from=base /wheeley /wheeley
COPY ./binaries /app/binaries

RUN pip3 install --no-index --find-links=/wheeley brewblox-devcon-spark \
    && rm -rf /wheeley \
    && pip3 freeze

ENTRYPOINT ["python3", "-m", "brewblox_devcon_spark"]