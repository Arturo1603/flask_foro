# Boilerplate Flask Final

### Entorno virtual

#### Creación

```sh
python -m venv venv
```

#### Activar

```sh
source venv/Scripts/activate -> Windows
source venv/bin/activate -> Linux / MacOS
```

### Dependencias

```python
pip install -r requirements.txt
```

#### Crear requirements (Ejecutar siempre que se instale una dependencia)

```python
pip freeze > requirements.txt
```

### Variables de Entorno

```python
FLASK_ENV='development'
FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000


DATABASE_URL='postgresql://postgres:mysql@localhost:5432/flask_boilerplate'

JWT_SECRET='tecsup'

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME='usuario@gmail.com'
MAIL_PASSWORD='password_aplicacion'

AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_REGION=''

MERCADOPAGO_MAIN_ACCESS_TOKEN=''
```

##### PostgreSQL URI

```python
            usuario:password@ip_servidor:puerto/nombre_db
postgresql://postgres:mysql@localhost:5432/flask_boilerplate
```

### Migrate (alembic)

```sh
flask db init -> Iniciamos
```

```sh
flask db migrate -m "Comentario" -> Crear una migración
```

```sh
flask db upgrade -> Subimos los cambios a la base de datos
```

#### Flask Restx

- Validar y documentar los query params, headers y form data

```http
https://flask-restx.readthedocs.io/en/latest/parsing.html
```

- Validar y documentar los request body

```http
https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
```

- Configuración de JWT

```http
https://flask-jwt-extended.readthedocs.io/en/stable/options/#general-options
```

- Tipos de datos en los Modelos (SQLAlchemy)

```http
https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html
```

# Deploy en Heroku

## Logearse

```sh
heroku login
```

## Crear Aplicación

```sh
- heroku create -> Nombre random
- heroku create nombre_aplicacion -> Nombre a elección
```

## Agregar Variables de entorno

```sh
heroku config:set ENV=value
```

## Agregar PostgreSQL a la aplicación

```sh
heroku addons:create heroku-postgresql:hobby-dev
```

## Desplegar

```sh
git push heroku main
```

## Ejecutar migraciones

```sh
heroku run flask db upgrade
```

## Ejecutar seeders

```sh
despliege -> heroku run flask seed run
local -> flask seed run
```
