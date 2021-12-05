import csv
from flask import Flask, jsonify
from flask_restful import Api
from models.movie import Movie
from models.tag import Tag
from models.link import Link
from models.rating import Rating
from services.get_movies import get_movies

app = Flask(__name__)
api = Api(app)

movies = get_movies("/Users/agnieszka/Desktop/movies.csv")

tags = []

with open("/Users/agnieszka/Desktop/tags.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for i, line in enumerate(reader):
        tag = Tag(line[0], line[1], line[2], line[3])
        tags.append(tag.__dict__)

links = []

with open("/Users/agnieszka/Desktop/links.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for i, line in enumerate(reader):
        link = Link(line[0], line[1], line[2])
        links.append(link.__dict__)

ratings = []

with open("/Users/agnieszka/Desktop/ratings.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for i, line in enumerate(reader):
        rating = Rating(line[0], line[1], line[2], line[3])
        ratings.append(rating.__dict__)


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
