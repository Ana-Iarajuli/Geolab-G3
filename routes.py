from flask import render_template, redirect
from forms import RegisterForm, MovieForm
from ext import app, db
from models import Movie
from os import path #operation system


profiles = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "gender": form.gender.data,
            "country": form.country.data
        }
        print("--------------------------")
        image = form.image.data
        # directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(f"{app.root_path}\\static\\images\\{image.filename}")
        new_user["profile_image"] = image.filename
        profiles.append(new_user)
        print(profiles)
    # print(form.errors)
    # print(form.username.data, form.password.data)
    return render_template("register.html", form=form)


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    return render_template("profile.html", profile=profiles[profile_id])


@app.route("/movies")
def movies():
    movie_list = Movie.query.all()
    return render_template("movies.html", movie_list=movie_list, role="admin")


@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template("movie.html", movie=movie)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie = Movie(name=form.name.data, release_year=form.release_year.data)
        image = form.image.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)
        new_movie.image = image.filename

        #add to database
        Movie.add(new_movie)

        return redirect("/movies")


    return render_template("add_movie.html", form=form)


@app.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get(movie_id)
    form = MovieForm(name=movie.name, release_year=movie.release_year, image=movie.image)
    print(form.image.data)
    if form.validate_on_submit():
        movie.name = form.name.data
        movie.release_year = form.release_year.data

        image = form.image.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)
        movie.image = image.filename

        Movie.save()

        return redirect("/movies")

    return render_template("edit_movie.html", form=form)


@app.route("/delete_movie/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    Movie.delete(movie)

    return redirect("/movies")