import random
import csv
import networkx as nx
from collections import deque
obj = csv.reader(open('data.csv', 'r'))
l = []  # nodelist
e = []  # edgelist
next(obj)
G = nx.DiGraph()  # directed graph
for row in obj:
    b = row[1][0:11].upper()
    l.append(b)  # appending nodes to nodelist
    for i in row[2:]:
        e.append((b, i[-11:].upper()))  # appending edges to edgelist
G.add_nodes_from(l)  # adding nodes to graph
G.add_edges_from(e)  # adding edges to graph

# Function to find the minimum degree of separation between two nodes in the graph
def separation(G, source, target):
    if not G.has_node(source) or not G.has_node(target):
        return -1

    visited = set()  # Set to store visited nodes
    queue = deque([(source, 0)])  # Queue to store nodes to visit
    visited.add(source)  # Add source node to visited set

    while queue:
        node, level = queue.popleft() 
        if node == target:
            return level
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return -1  # Target node not reachable


# Function to compute average minimum degree of separation between all possible node pairs
def avg_separation_all_pairs(G):
    total_min_degree = 0
    num_pairs = 0
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            source = nodes[i]
            target = nodes[j]
            min_degree = separation(G, source, target)
            if min_degree != -1:
                total_min_degree += min_degree
                num_pairs += 1

    return total_min_degree / num_pairs if num_pairs != 0 else 0


# Compute and print the average minimum degree of separation
avg_min_degree_all_pairs = avg_separation_all_pairs(G)
print("Average Minimum Degree of Separation between all possible node pairs:", avg_min_degree_all_pairs)
