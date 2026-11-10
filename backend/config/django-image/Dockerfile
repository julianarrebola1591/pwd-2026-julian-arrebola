FROM python:3.12-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev libgdal-dev graphviz-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN mkdir /scripts
COPY runserver.sh /scripts
RUN chmod +x /scripts -R

CMD ["/scripts/runserver.sh"]
