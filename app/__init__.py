from flask import Flask, request, session, render_template, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps
# from flask_login import LoginManager
from config import Config
from app.models.user import User
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
# app.config['SECRET_KEY'] = 'your-secret-key'
# db = SQLAlchemy(app)
# db.init_app(app)


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    from app.extensions import init_extensions
    init_extensions(app)  

    

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)


    @app.route('/admin')
    def admin_page():
        return render_template('admin.html')


    @app.route('/staff')
    def staff_page():
        return render_template('staff.html')
    
    return app


# # login required decorator
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('login'))
#     return wrap


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)