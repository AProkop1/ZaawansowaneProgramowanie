from flask_restful import Resource


class Tag(Resource):
    def __init__(self, user_id: str, movie_id: str, tag: str, timestamp: str):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

    def get(self):
        return {'user id': self.user_id,
                'movie id': self.movie_id,
                'tag': self.tag,
                'timestamp': self.timestamp}
