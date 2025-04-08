import csv

class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def import_csv(filename):
    nodes = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # başlığı atla
        for row in reader:
            if len(row) < 4:  # satır eksikse atla
                continue
            id = row[0]
            name = row[3]
            nodes.append(Node(id, name))
    return nodes


