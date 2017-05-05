from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Создаём объект приложения
app = Flask(__name__)

app.config.from_object('config')
app.static_folder = 'static'

# База данных
db = SQLAlchemy(app)

from app import views, models
