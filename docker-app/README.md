# Topics

## Part I

- [x] ~~*Installation*~~ [2022-05-02]
- [x] ~~*Basic application structure*~~ [2022-05-06]
- [x] ~~*Templates*~~ [2022-05-11]
- [x] ~~*Web Forms*~~ [2022-05-12]
- [ ] Databases
- [ ] Email
- [ ] Large Application Structure

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

### Requirements.txt
    - flask
    - flask-bootstrap
    - flask-moment
    - flask-wtf