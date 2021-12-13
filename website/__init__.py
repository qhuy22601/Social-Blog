from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO()
def createapp():
    app = Flask(__name__)
    from .views import views
    app.register_blueprint(views, url_prefix ="/")
    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:191916823@localhost/Social_blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)
    loginManager = LoginManager(app)
    loginManager.login_view = "/"
    socketio.init_app(app)

    from  .models import Users

    createdatabase(app)

    @loginManager.user_loader
    def userLoaded(id):
        return Users.query.filter_by(id =int(id)).first()
    return socketio, app

def createdatabase(app):
    if not path.exists("website/database.db"):
        db.create_all(app = app)
        print("Created")