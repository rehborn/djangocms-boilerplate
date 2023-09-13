# DjangoCMS Boilerplate

Pre-heated Boilerplate with common defaults to get started quickly

### Features

- Pre-build Docker Image with DjangoCMS
- Pre-themed with Bootstrap-5, Font-Awesome and Simple-Icons 
- minimal site configuration in yaml `config.yml`

### Pre-installed plugins
- teams

see [Roadmap](#1) for planned features

## Customization

minimal configuration can be found in [`example/`](example):

- [`config.yml`](example/config.yml): minimal configuration wrapper
- `static`: static and theme files (`theme.scss`, `theme.js`)
- `templates`: custom templates (page templates defined in `config.yml` and overwrite defaults)

### Templates

place templates in `config/templates/`

defaults that can be overwritten:

```
- base.html: defined blocks `title`, `css`, `content`, `js`
  - css.html: 
  - header.html
  - navigation.html
    - nav-items.html
    - languages.html
  - footer.html
```

#### default content templates (`CMS_TEMPLATES`):
- `default.html`
- `single-page.html` (render all plugins of sub-pages)


#### Images depending on `prefers-color-scheme` (aka Dark Mode) 
```html
<img alt="logo" src="{% static 'logo.png' %}" class="logo" data-logo-light="{% static 'logo.png' %}" data-logo-dark="{% static 'logo-dark.png' %}" />
```

### Static

#### Style (SCSS)

`theme.scss`
```scss
/* custom theme */

// custom css

@import "../../node_modules/bootstrap/scss/bootstrap";
```


#### default static files that can be overwritten

- `logo.png`
- `favicon.ico`
- `theme.scss` 
- `extras.css`
- `theme.js`

## Workflow

#### Setup new Instance
```
cp -R example/ config/
docker compose up -d
docker compose exec cms poetry run python /app/src/manage.py migrate
docker compose exec cms poetry run python /app/src/manage.py boil
```
- http://127.0.0.1:8000/admin/

> `demo`:`demo`

**Update UserSettings**
- http://127.0.0.1:8000/admin/base/usersettings/



## Deployment

see `docker-compose-test.yml` for orientation (do not use in production)

## Development

### Setup

#### Install Dependencies
```shell
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

## Declare independence

if at any point you decide to break out of the constraints of this projects or remove it as a dependency to bake your 
own, you can follow these vague steps (_untested_):

- fork repository 
- remove use of `env()` and `config()` in `settings.py`
- migrate values of `config.yml` to `settings.py`
- move templates from `config/templates` to `src/templates/`
- move static files from `config/static` to `src/static/`
- create and publish your own docker image
- update `image:` in your deployment



## Dependencies

this project wouldn't be possible without open source

### Frameworks
- [Django](https://github.com/django/django)
- [DjangoCMS](https://github.com/django-cms/django-cms)

for a full list see [pyproject.toml](pyproject.toml)

### Theme
- [Boostrap](https://github.com/twbs/bootstrap)
- [Font Awesome](https://github.com/FortAwesome/Font-Awesome)
- [Simple Icons](https://github.com/simple-icons/simple-icons)
- [Flag Icons](https://www.npmjs.com/package/flag-icons)

for a full list see [package.json](package.json)

