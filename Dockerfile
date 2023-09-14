FROM python:3.11

ENV NODE_MAJOR=20

ENV DEBUG=False

ENV APP_DIR=/app
ENV CONF_DIR=/config
ENV STATIC_DIR=/static

WORKDIR ${APP_DIR}

COPY package.json package-lock.json pyproject.toml poetry.lock ${APP_DIR}

RUN apt update && apt install ca-certificates curl gnupg -y && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list

RUN apt update && apt install gettext nodejs -y && pip install poetry && poetry install && npm install

ADD src ${APP_DIR}/src
ADD example /config
WORKDIR ${APP_DIR}/src

RUN poetry run python manage.py compilemessages

# cleanup
RUN apt remove ca-certificates curl gnupg nodejs -y && \
    rm -rf /var/lib/apt/lists/* /var/log/* /var/lib/dpkg/info/*

EXPOSE 80

CMD ["poetry", "run", "gunicorn", "--bind", ":80", "base.wsgi:application"]
