# app/__init__.py

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import Flask
from werkzeug import SharedDataMiddleware
from config import config

# extension
from .extensions import mail, login_manager, db

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)


    app.add_url_rule('/uploads/<filename>', 'uploads', build_only=True)
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/uploads':  app.config['UPLOAD_FOLDER']
    })


    from .ex import ex
    app.register_blueprint(ex)

    return app
