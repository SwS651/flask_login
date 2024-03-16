
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from flask import create_app
db = SQLAlchemy()
login_manager = LoginManager()
    
def init_extensions(app):
    db.init_app(app)
    with app.app_context():
        #Create database
        db.create_all()

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
