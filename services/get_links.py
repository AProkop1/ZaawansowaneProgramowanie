import csv
from models.link import Link


def get_links(path):
    links = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for i, line in enumerate(reader):
            link = Link(line[0], line[1], line[2])
            links.append(link.__dict__)