from ext import app


if __name__ == "__main__":
    from routes import home, about, register, movies, profile, movie_details
    app.run(debug=True)