# Important info

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

## Installations
    - flask
    - flask-bootstrap
    - flask-moment
    - flask-wtf
    - flask-sqlalchemy