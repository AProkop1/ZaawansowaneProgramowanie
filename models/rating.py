from flask_restful import Resource


class Rating(Resource):
    def __init__(self, user_id: str, movie_id: str, rating: str, timestamp: str):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def get(self):
        return{'user id': self.user_id,
               'movie id': self.movie_id,
               'rating': self.rating,
               'timestamp': self.timestamp}