FROM python:3.11

WORKDIR /app

COPY package.json package-lock.json pyproject.toml poetry.lock /app/

ENV NODE_MAJOR=20

RUN apt update && apt install ca-certificates curl gnupg -y && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list

RUN apt update && apt install gettext nodejs -y && pip install poetry && poetry install && npm install

ADD src /app
ADD example /config

RUN echo "DEBUG=False\nAPP_DIR=/app" > /app/.env

# RUN poetry run python /app/src/manage.py compilemessages && poetry run python /app/src/manage.py collectstatic --noinput

# cleanup
RUN apt remove ca-certificates curl gnupg nodejs -y && \
    rm -rf /var/lib/apt/lists/* /var/log/* /var/lib/dpkg/info/*


CMD ["poetry", "run", "gunicorn", "--bind", ":8000", "base.wsgi:application"]
