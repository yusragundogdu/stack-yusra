import csv

class Node:
    def __init__(self, id, latitude, longitude, name):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

def import_csv(filename):
    nodes = []
    try:
        with open(filename, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)  
            for row in csv_reader:
                node_id = row['id']
                latitude = float(row['lattitude'])
                longitude = float(row['longtitude'])
                name = row['name']
                node = Node(node_id, latitude, longitude, name)
                nodes.append(node)
    except FileNotFoundError:
        print(f"Hata: '{filename}' dosyası bulunamadı.")
    return nodes

if __name__ == '__main__':
    node_listesi = import_csv("coordinates.csv")
    for node in node_listesi:
        print(f"ID: {node.id}, Name: {node.name}, Latitude: {node.latitude}, Longitude: {node.longitude}")