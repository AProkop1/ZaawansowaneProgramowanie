import csv
from models.tag import Tag


def get_tags(path):
    tags = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for i, line in enumerate(reader):
            tag = Tag(line[0], line[1], line[2], line[3])
            tags.append(tag.__dict__)
