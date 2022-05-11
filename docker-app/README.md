# Topics

## Part I

- [x] ~~*Installation*~~ [2022-05-02]
- [x] ~~*Basic application structure*~~ [2022-05-06]
- [ ] Templates
- [ ] Web Forms
- [ ] Databases
- [ ] Email
- [ ] Large Application Structure

## Part II

- [ ] User Authentication

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

### Requirements.txt
    - flask
    - flask-bootstrap
    - flask-moment