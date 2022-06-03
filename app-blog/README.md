# Topics

## Part I

- [x] ~~*Installation*~~ [2022-05-02]
- [x] ~~*Basic application structure*~~ [2022-05-06]
- [x] ~~*Templates*~~ [2022-05-11]
- [x] ~~*Web Forms*~~ [2022-05-12]
- [x] ~~*Databases*~~ [2022-05-17]
- [x] ~~*Email*~~ [2022-05-18]
- [x] ~~*Large Application Structure*~~ [2002-05-30]

## Part II

- [ ] User Authentication
- [ ] User Roles
- [ ] User Profiles
- [ ] Blog Posts
- [ ] Followers
- [ ] User Comments
- [ ] Application Programming Interfaces

## Part III

- [ ] Testing
- [ ] Performance
- [ ] Deployment
- [ ] Additional Resources

## Steps

### Installation and Basic application structure:
    - python -m venv venv
    - venv\Scripts\activate.bat
    - create requirements.txt file:
        - set flask
        - pip install -r requirements.txt
    - set FLASK_APP=app.py (or export)
    - set FLASK_DEBUG=1
    - flask run
    - dynamic routes

### Useful commands
    - from flask
        - Flask (The main instance)
        - make_response()
        - abort()
        - redirect()
        - render_template()
        - session
        - url_for()
        - flash()
    - from context
        - current_app
        - g
        - request
        - session
    - from request
        - form
        - args
        - cookies
        - headers
        - file
        - get_data()
        - get_json()
        - blueprint
        - endpoint
        - method
        - scheme
        - is_secure
        - host
        - path
        - query_string
        - full_path
        - url
        - base_url
        - remote_addr
        - environ
    - request hooks
        - before_request
        - before_first_request
        - after_request
        - teardow_request
    - from response
        - status_code
        - headers
        - set_cookie()
        - delete_cookie()
        - content_length
        - content_type
        - set_data()
        - get_data()
        
### Templates
    - Jinja variables filters
        - safe
        - capitalize
        - lower
        - upper
        - title
        - trim
        - striptags
    - Jinja Links and static files
        - "{{url_for('user', name=item, _external=True)}}"
        - <img src="{{url_for('static', filename=item+'.jpg', _external=True)}}" class="card-img-top" alt="...">

### Moment 
    - Pass the argument like return render_template('index.html', name=name, list_of_items=list_of_items, current_time=datetime.utcnow())
    - {{moment.include_moment()}}
    - <p>The local date and time is {{moment(current_time).format('LLL')}}</p>
    - <p>That was {{moment(current_time).fromNow(refresh=True)}}</p>

### Web Forms

We can add (and should) "wtforms" with the type of fields in our form and we can add "wtforms.validators" like a DataRequired. The general steps are: Create the Class Form, Implements the class form in the view, design the styles for the form, create a sessions values and message flashing.

We can put the flash messages in the base html using the bootstrap dismissing. 

    - Standard HTML Fields
        - BooleanField
        - DateField
        - DateTimeField
        - DecimalField
        - FileField
        - HiddenField
        - MultipleFileField
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
    - Wtform validators
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

### DataBases

#### Databases engines

    - MySQL
    - Postgres
    - SQLite

#### Steps for setting up the database:

    - from flask_sqlalchemy import SQLAlchemy
    - Take the basedir 
    - App config:
        - SQLALCHEMY_BATABASE_URI
        - SQLALCHEMY_TRACK_MODIFICATIONS
    - Create db instance 

#### Model Definition and most common Type names:

    - Create the model definition inheriting of db
    - Integer -> int
    - SmallInteger -> int
    - BigInteger -> int or long
    - Float -> float
    - Numeric -> decimal.Decimal
    - String -> str
    - Text -> str
    - Unicode -> unicode
    - UnicodeText -> unicode
    - Boolean -> bool
    - Date --> datetime.time
    - Time -> datetime.time
    - DateTime -> datetime.datetime
    - Interval -> datetime.timedelta
    - Enum -> str
    - PickleType -> Any python object
    - LargeBinary -> str

#### Attributes: 

    - primary_key
    - unique
    - index 
    - nullable
    - default

#### Relathionships

    - backref
    - primaryjoin
    - lazy
    - uselist
    - order_by
    - secondary
    - secondaryjoin

### Databases operations

    - Create Tables
        - flask shell
        - from flasky import db
        - db.create_all()
        - db.drop_all()
        - db.create_all()

    - Inserting rows
        - from flasky import Role, User
        - admin_role = Role(name='Admin')
        - user_susan = User(username='Susan', role=admin_role)
        - db.session.add(admin_role)
        - db.session.add(user_susan)
        - db.session.add_all([admin_role, user_susan])
        - db.session.commit()
    
    - Modifying rows
        - admin_role.name = 'Administrator'
        - db.session.add(admin_role)
        - db.session.commit()
    
    - Deleting rows
        - db.session.delete(mod_role)
        - db.session.commit()
        - db.session.rollback()

    - Querying rows
        - Role.query.all()
        - User.query.all()
        - User.query.filter_by(role=user_role).all()
        - str(User.query.filter_by(role=admin_role))
        - user_role = Role.query.filter_by(name='Susan').first()

### Common Query filters

    - filter()
    - filter_by()
    - limit()
    - offset()
    - order_by()
    - group_by()

### Common query options

    - all()
    - first()
    - first_or_404()
    - get()
    - get_or_404()
    - count()
    - paginate()

### Databases Migrations

    - flask db init
    - flask db migrate -m "initial migration"
    - flask db upgrade

### Email
Flask-Mail SMTP server configuration keys

    - MAIL_SERVER -> localhost
    - MAIL_PORT -> 25
    - MAIL_USE_TLS -> False
    - MAIL_USE_SSL -> False
    - MAIL_USERNAME -> None
    - MAIL_PASSWORD -> None

## setup first and basic structure

- web-app
    - app
        - main
            - \_\_init\_\_.py : Blueprint information
            - errors.py 
            - forms.py
            - views.py : Create the routes 
        - static
        - templates
            - base
            - errors
            - mail
            - index.html
        - \_\_init\_\_.py : Create the app kernel
        - email.py
        - models.py
    - migrations
    - tests
        - \_\_init\_\_.py
        - test_basic.py : Basic test
    - venv
    - .env : The setup information
    - .gitignore
    - config.py : Retrieve the setup information
    - flasky.py : Create app and setup test information
    - README.md
    - requirements.txt

## Security

### werkzeug's
    - generate_password_hash(password, method = 'pbkdf2:sha56', salt_length = 8)
    - check_password_hash(hash, password)

### flask-login
    validate_ : the prefix followed by the name of a field, the mothod is invoked in addition to any regularly defined validators

### Requirements.txt
    - flask
    - flask-bootstrap
    - flask-moment
    - flask-wtf
    - flask-sqlalchemy
    - flask-migrate
    - flask-mail
    - python-dotenv
    - flask-login