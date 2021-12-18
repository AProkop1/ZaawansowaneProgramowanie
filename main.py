from flask import Flask, jsonify
from flask_restful import Api
from services.get_movies import get_movies
from services.get_tags import get_tags
from services.get_links import get_links
from services.get_ratings import get_ratings

app = Flask(__name__)
api = Api(app)

movies = get_movies("movies.csv")

tags = get_tags("tags.csv")

links = get_links("links.csv")

ratings = get_ratings("ratings.csv")


class Movies(Resource):
    def get(self):
        return jsonify(movies)

api.add_resource(Movies, '/movies')


class Links(Resource):
    def get(self):
        return jsonify(links)

api.add_resource(Links, '/links')


class Ratings(Resource):
    def get(self):
        return jsonify(ratings)

api.add_resource(Ratings, '/ratings')


class Tags(Resource):
    def get(self):
        return jsonify(tags)

api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
