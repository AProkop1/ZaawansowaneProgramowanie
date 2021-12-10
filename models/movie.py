from flask_restful import Resource


class Movie(Resource):
    def __init__(self, movie_id: str, title: str, genres: str):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres

    def get(self):
        return{'id': self.movie_id,
               'title': self.title,
               'genres': self.genres}



