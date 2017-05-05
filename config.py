import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Путь к файлу с нашей базой данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# Папка для хранения файлов SQLAlchemy-migrate
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
