# Topics
- [x] ~~*Installation*~~ [2022-05-02]
- [ ] Basic application structure
- [ ] Templates
- [ ] Web Forms

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

### Requirements.txt
    - flask