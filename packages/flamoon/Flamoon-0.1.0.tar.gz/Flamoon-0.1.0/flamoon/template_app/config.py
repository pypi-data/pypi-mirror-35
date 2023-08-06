# config.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os
from dotenv import load_dotenv

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', default=os.urandom(32))
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY', default=os.urandom(32))

    # включение / отключение CSRF
    WTF_CSRF_ENABLED = True

    FLASK_COVERAGE = True

    # отслеживание изменений объектов и подача сигналов
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # путь загрузки файлов
    UPLOAD_FOLDER = basedir + '/uploads'
    # разрешонные расширения для изображений
    ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif', '.svg'])

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    APP_MAIL_SENDER = 'your@gmail.com'
    APP_ADMIN = os.environ.get('APP_ADMIN', default='admin@gmail.com') 
    APP_MODERATOR = os.environ.get('APP_MODERATOR', default='moderator@gmail.com')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', default='test')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', default='test123')
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    @staticmethod
    def init_app(app): pass

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class DevelopmentConfig(Config):
    # включение / отключение отладчика
    FLASK_DEBUG = True

    # путь к файлу к базе данных.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

    # путь к файлу к базе данных.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 
        'data_test.sqlite')

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}