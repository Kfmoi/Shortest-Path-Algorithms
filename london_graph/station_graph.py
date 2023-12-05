from math import radians, sin, cos, sqrt, atan2
from given_code.final_project_part1 import DirectedWeightedGraph
import csv


# calculate distance using haversine formula to get ‘as-the-crow-flies’ distance,
# takes into account Earth's spherical shape (regular distance formula also works in this case)
def distance(lat1, lon1, lat2, lon2):
    Radius = 6371

    diff_lat = radians(lat2 - lat1)
    diff_lon = radians(lon2 - lon1)
    lat1_rad = radians(lat1)
    lat2_rad = radians(lat2)

    a = sin(diff_lat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(diff_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    dist = Radius * c
    return dist


def load_connections(file_path):
    connections_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            connections_data.append({
                'station1_id': int(row['station1']),
                'station2_id': int(row['station2']),
                'line': int(row['line']),
                'time': int(row['time'])
            })
    return connections_data


def load_stations(file_path):
    stations_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations_data.append({
                'id': int(row['id']),
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude'])
            })
    return (stations_data)


def create_graph(stations_data, connections_data):
    G = DirectedWeightedGraph()

    for station in stations_data:
        G.add_node(station['id'])

    for connection in connections_data:
        node1 = connection['station1_id']
        node2 = connection['station2_id']

        weight = connection['time']

        G.add_edge(node1, node2, weight)
        G.add_edge(node2, node1, weight)

    return G


def create_london_subway_graph():
    c = load_connections('../Data/london_connections.csv')
    s = load_stations('../Data/london_stations.csv')
    g = create_graph(s, c)
    return g

# Sample Tests for station 11 and 163
# g = create_london_subway_graph()
# c = load_connections('../Data/london_connections.csv')
# s = load_stations('../Data/london_stations.csv')
# print(g.w(s[9]['id'],s[142]['id'] ))
# print(g.w(s[142]['id'],s[9]['id'] ))
# print(g.are_connected(s[9]['id'], s[142]['id']))
# print(g.adjacent_nodes(s[142]['id']))
