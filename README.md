# DjangoCMS Boilerplate

Pre-heated Boilerplate with common defaults to get started quickly

### features

- Pre-build Docker Image with DjangoCMS
- Pre-themed with Bootstrap-5, Font-Awesome and Simple-Icons 
- minimal site configuration in yaml `config.yml`

### plugins
- teams

## Customization

`example/`:
- `config.yml`: minimal configuration wrapper
- `static`: static files (css, js, images)
- `templates`: custom templates (page templates defined in `config.yml` and overwrite defaults)

### default templates
```
- base.html: defined blocks `title`, `css`, `content`, `js`
  - css.html: 
  - header.html
  - navigation.html
    - nav-items.html
    - languages.html
  - default.html
  - footer.html
```
default content template: `default.html`

### default static files
- `logo.png`
- `favicon.ico`
- `theme.css`
- `theme.js`

## Deployment

#### Docker Volumes

- optional: postgres (path or remote host)
- optional: config.yml, templates (path or private s3 bucket)

- optional: theme (path or private s3 bucket)
- optional: media (path or public s3 bucket)


## Development

### Setup

#### Install Dependencies
```shell
pip install poetry
poetry install
npm install
```

#### Initialize CMS
```shell
cp -R example/ config
./manage.py migrate
./manage.py cms check
./manage.py boil
```

#### run postgres and redis using docker
```shell
docker compose up postgres
docker compose up redis
```

#### run commands inside container
```shell
docker compose exec cms poetry run python /app/manage.py migrate
docker compose exec cms poetry run python /app/manage.py boil
```

### Test Deployment

#### Build Image
```shell
docker compose build --no-cache
```

#### Run Container
```shell
docker compose -f docker-compose-test.yml up
```

#### Shortcuts
```shell
docker compose -f docker-compose-test.yml run job-migrate
docker compose -f docker-compose-test.yml run job-once
docker compose -f docker-compose-test.yml exec static ls /usr/share/nginx/html/{static,media}
docker compose -f docker-compose-test.yml exec cms poetry run python /app/manage.py boil
docker compose -f docker-compose-test.yml exec cms bash
```

## Dependencies
- Django
- DjangoCMS
- Boostrap5
- font-awesome-free
- django-modeltranslation
- https://www.npmjs.com/package/flag-icons
