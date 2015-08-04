SECRET_KEY = '\xe2\xe7A\x92\xcftl\@\xb3\xc8\x83\xc4\xad\xe9'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_FILE = 'app.db'
DATABASE_PATH = os.path.join(basedir, DATABASE_FILE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_ECHO = True
