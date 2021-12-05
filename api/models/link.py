from flask_restful import Resource


class Link(Resource):
    def __init__(self, movie_id: str, imdb_id: str, tmbd_id: str):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmbd_id = tmbd_id

    def get(self):
        return{'id': self.movie_id,
               'imdb_id': self.imdb_id,
               'tmbd_id': self.tmbd_id}