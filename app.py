from ext import app


if __name__ == "__main__":
    from routes import home, register, movie_details
    app.run(debug=True)