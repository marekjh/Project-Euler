import numpy as np

def main():
    graph = build_graph("../data/matrix.txt")
    print(shortest_path(graph))
    
# Implementation of Dijkstra's Algorithm
def shortest_path(graph):
    start = graph[0][0]
    start.dist = start.value
    endpoint = graph[-1][-1]
    nodes = Queue()
    for row in graph:
        for node in row:
            nodes.add(node)
    while not nodes.is_empty():
        n = nodes.get()
        for m in n.next:
            new_dist = n.dist + m.value
            if new_dist < m.dist:
                m.dist = new_dist
    return endpoint.dist

def build_graph(file):
    with open(file) as f:
        M = [[int(x) for x in y.split(",")] for y in f.readlines()]
    size = len(M)
    M = np.array([[Node(e) for e in row] for row in M])
    for i in range(size):
        for j in range(size):
            n = M[i][j]
            if i > 0:
                n.connect(M[i-1][j])
            if i < size-1:
                n.connect(M[i+1][j])
            if j > 0:
                n.connect(M[i][j-1])
            if j < size-1:
                n.connect(M[i][j+1])
    return M


class Node():
    def __init__(self, value):
        self.value = value
        self.dist = np.inf
        self.next = []
    
    def connect(self, other):
        self.next.append(other)
    
    def __lt__(self, other):
        return self.dist < other.dist
    
    def __repr__(self):
        return str(self.value)
    
class Queue():
    def __init__(self):
        self.queue = [] 
        
    def add(self, e):
        self.queue.append(e)
    
    def get(self):
        closest = min(self.queue)
        self.queue.remove(closest)
        return closest
    
    def is_empty(self):
        return len(self.queue) == 0

if __name__ == "__main__":
    main()