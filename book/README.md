# Important info

## Most used types in url
/path/<type:variable>
    - string 
    - int
    - float
    - path

## Global context
    - current_app
    - g
    - request
    - session

## Request context
    - form
    - args
    - values
    - cookies
    - headers
    - files
    - get_data()
    - get_json()
    - blueprint
    - endpoint
    - method
    - scheme
    - is_secure()
    - host
    - path
    - query_string
    - full_path
    - url
    - base_url
    - remote_addr
    - environ

## Request Hooks
    - before_request
    - before_first_request
    - after_request
    - teardow_request

## Flask Response object
    - status_code
    - headers
    - set_cookie()
    - delete_cookie()
    - content_length
    - content_type
    - set_data()
    - get_data()

## Useful functions
    - make_response()
    - abort()
    - redirect()
    - render_template()
    - url_for()
    - session['name']
    - Blueprint

## Jinja2 Filters (some)
    - safe
    - capitalize
    - lower
    - upper
    - title
    - trim 
    - striptags

## flask-moment
    - based in moment.js

## flask-wtf (Forms)

### Fields
    - BooleanField
    - DateField
    - DateTimeField
    - DecimalField
    - FileField
    - HiddenField
    - MultipleField
    - FieldList
    - FloatField
    - FormField
    - IntegerField
    - PasswordField
    - RadioField
    - SelectField
    - SelectMultipleField
    - SubmitField
    - StringField
    - TextAreaField

### Validators
    - DataRequired
    - Email
    - EqualTo
    - InputRequired
    - IPAdress
    - Length
    - MacAdress
    - NumberRange
    - Optional
    - Regexp
    - URL
    - UUID
    - AnyOf
    - NoneOf

## Flask-SQLAlchemy

### Database Engine
    - MySQL
    - Postgres
    - SQLite

### Column Types
    - Integer
    - SmallInteger
    - BigInteger
    - Float
    - Numeric
    - String
    - Text
    - Unicode
    - UnicodeText
    - Boolean
    - Date
    - Time
    - DateTime
    - Interval
    - Enum
    - PickleType
    - LargeBinary

### SQLAlchemy common columns options
    - primary_key
    - unique
    - nullable
    - index
    - default

### SQLAlchemy common relationships options
    - backref
    - primaryjoin
    - lazy:
        - select
        - immediate
        - joined
        - subquery
        - noload
        - dynamic
    - uselist
    - order_by
    - secondary
    - secondaryjoin

### SQLAlchemy common operations with databases
    - db.create_all()
    - db.drop_all()
    - db.session.add(model)
    - db.session.add_all(list_of_values)
    - db.session.commit()
    - db.session.rollback()
    - db.session.delete()

### Querying rows
    - all()
    - first()
    - first_or_404()
    - get()
    - get_or_404()
    - count()
    - paginate()
    - filter()
    - filter_by()
    - limit()
    - offset()
    - order_by()
    - group_by()

## Flask Migrationes
    - flask bd init
    - flask db migrate -m "initial migration"
    - flask db upgrade
    - flask db downgrade

## Flask Mail
    - MAIL_SERVER
    - MAIL_PORT
    - MAIL_USE_TLS
    - MAIL_USE_SSL
    - MAIL_USERNAME
    - MAIL_PASSWORD

## Installations
    - flask
    - flask-bootstrap
    - flask-moment
    - flask-wtf
    - flask-sqlalchemy
    - flask-migrate
    - flask-mail

## Large app
    - app/
        - main/
            - __init__.py
            - errors.py
            - forms.py
            - views.py
        - static/
        - templates/
        - __init__.py
        - email.py
        - models.py
    - migrations/
    - tests/
    - .env
    - config.py
    - flasky.py
    - .gitignore
    - requirements.txt

For the large app is necessary make some configurations before to run the app.

### Modifications and reasons of each file
    - app/
        - main/
            - __init__.py -> Blueprint configuration to set a namespace
            - errors.py
            - forms.py
            - views.py -> Set views inside of their namespace
        - static/
        - templates/
        - __init__.py -> Create app, set app configuration and register blueprint
        - email.py
        - models.py
    - migrations/
    - tests/
    - .env
    - config.py
    - flasky.py
    - .gitignore
    - requirements.txt