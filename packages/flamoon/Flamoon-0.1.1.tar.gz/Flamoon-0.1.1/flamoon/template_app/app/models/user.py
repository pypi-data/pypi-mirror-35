# app/models/user.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from datetime import datetime
from flask import current_app, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .. import db, login_manager

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class User(UserMixin, db.Model):
    '''Создаёт пользователей'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    @property
    def password(self):
        '''Закрывает доступ на чтение пароля'''
        raise AttributeError('пароль не является читаемым атрибутом')


    @password.setter
    def password(self, password):
        '''Генерирует хеш из пароля'''
        self.password_hash = generate_password_hash(password)

    
    def verify_password(self, password):
        '''Сравнивает пполученный пароль с захешированным паролем 
        лежащим в базе данных'''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User - {}>'.format(self.username)




@login_manager.user_loader
def load_user(user_id):
    '''Принимает идентификатор в виде строки Юникода и, если указанный 
    идентификатор существует, возвращает объект, представляющий пользователя, 
    в противном случае возвращается None''' 
    return User.query.get(int(user_id))
