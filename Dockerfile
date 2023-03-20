FROM python:3.11-slim as base

RUN adduser --disabled-password pynecone


FROM base as build

WORKDIR .
#ENV VIRTUAL_ENV=/app/venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y gcc python3-dev
RUN pip install psutil
RUN pip install -r requirements.txt


FROM base as runtime

RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_19.x | bash - \
    && apt-get update && apt-get install -y \
    nodejs \
    unzip \
    && rm -rf /var/lib/apt/lists/*

#ENV PATH="$PATH:$PATH"


FROM runtime as init

WORKDIR .
#ENV BUN_INSTALL="/.bun"
COPY --from=build . .

RUN pc init


FROM runtime

COPY --chown=pynecone --from=init . .
USER pynecone
WORKDIR .

CMD ["pc","run" , "--port", "9000"]

EXPOSE 3000
EXPOSE 9000