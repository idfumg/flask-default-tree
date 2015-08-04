from app import app
from config import DATABASE_PATH
import os

def build_db():
    db.drop_all()
    db.create_all()

    # building database

    db.commit()

if __name__ == '__main__':
    if not os.path.exists(DATABASE_PATH):
        build_db()

    app.run(debug=True)
