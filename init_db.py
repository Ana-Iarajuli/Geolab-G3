from ext import app, db
from models import Movie, User, Review

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username="admin", password="adminpass", role="Admin")
    admin.create()