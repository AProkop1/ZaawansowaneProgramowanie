from flask import Flask, jsonify
from flask_restful import Api
from services.get_movies import get_movies
from services.get_tags import get_tags
from services.get_links import get_links
from services.get_ratings import get_ratings

app = Flask(__name__)
api = Api(app)

movies = get_movies("/Users/agnieszka/Desktop/movies.csv")

tags = get_tags("/Users/agnieszka/Desktop/tags.csv")

links = get_links("/Users/agnieszka/Desktop/links.csv")

ratings = get_ratings("/Users/agnieszka/Desktop/ratings.csv")


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)


@app.route('/tags', methods=['GET'])
def get_tags():
    return jsonify(tags)


@app.route('/links', methods=['GET'])
def get_links():
    return jsonify(links)


@app.route('/ratings', methods=['GET'])
def get_ratings():
    return jsonify(ratings)


if __name__ == '__main__':
    app.run(debug=True)
