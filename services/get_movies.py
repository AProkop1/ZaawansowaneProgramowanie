from models.movie import Movie
import csv


def get_movies(path):
    with open(path, newline="", encoding="utf-8") as f:
        movies = []
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for i, line in enumerate(reader):
            movie = Movie(line[0], line[1], line[2])
            movies.append(movie.__dict__)
    return movies
