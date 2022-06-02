from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

moment = Moment()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.debug=1
    
    # init_app(app) configuration
    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    
    # print(f"Config: {app.config}")
    # attach routes and custom error pages here
    
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app