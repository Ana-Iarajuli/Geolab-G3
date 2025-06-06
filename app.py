from flask import Flask, render_template

app = Flask(__name__)

profiles = [
    {"name": "Jasurbeki", "surname": "Iaxshiboevi", "image": "cat.jpg"},
    {"name": "Iago", "surname": "Xvichia", "image": "cat2.jpg"}
]

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


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    if profile_id == 1:
        return render_template("profile.html", profile_id=profile_id, profile=profiles[0])
    return render_template("profile.html", profile_id=profile_id, profile=profiles[1])


@app.route("/movies")
def movies():
    return render_template("movies.html", movie_list=movie_list, role=role)


@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    return render_template("movie.html",
                           movie=movie_list[movie_id])


if __name__ == "__main__":
    app.run(debug=True)