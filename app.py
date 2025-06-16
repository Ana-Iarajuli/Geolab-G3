from flask import Flask, render_template
from forms import RegisterForm
from os import path #operation system

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"

profiles = []

movie_list = [
    {"id": 0,
    "name": "Game of Thrones", "genre": "Action Epic", "image": "https://m.media-amazon.com/images/M/MV5BMTNhMDJmNmYtNDQ5OS00ODdlLWE0ZDAtZTgyYTIwNDY3OTU3XkEyXkFqcGc@._V1_QL75_UX140_CR0,1,140,207_.jpg"},
    {"id": 1,
     "name": "Dept. Q", "genre": "Drama", "image": "https://m.media-amazon.com/images/M/MV5BNWQ3MDQ2MGQtOGM0MC00MzlkLWE0ODQtYzE4Zjc3Mjc1ZWI5XkEyXkFqcGc@._V1_QL75_UY207_CR13,0,140,207_.jpg"},
    {"id": 2,
     "name": "The last of us", "genre": "Apocalyptic", "image": "https://m.media-amazon.com/images/M/MV5BYWI3ODJlMzktY2U5NC00ZjdlLWE1MGItNWQxZDk3NWNjN2RhXkEyXkFqcGc@._V1_QL75_UX140_CR0,0,140,207_.jpg"}
]

role = "guest"


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
    return render_template("movies.html", movie_list=movie_list, role=role)


@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    return render_template("movie.html",
                           movie=movie_list[movie_id])


if __name__ == "__main__":
    app.run(debug=True)