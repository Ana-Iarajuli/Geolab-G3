from ext import db
from sqlalchemy import ForeignKey


class BaseModel:
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()


class Movie(db.Model, BaseModel):
    __tablename__ = "movies"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    release_year = db.Column(db.Integer(), nullable=False)
    image = db.Column(db.String(), default="default_photo.jpg")


class Review(db.Model, BaseModel):
    __tablename__ = "reviews"

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(), nullable=False)
    movie_id = db.Column(ForeignKey("movies.id"))