import csv
from models.rating import Rating


def get_ratings(path):
    ratings = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for i, line in enumerate(reader):
            rating = Rating(line[0], line[1], line[2], line[3])
            ratings.append(rating.__dict__)
    return ratings