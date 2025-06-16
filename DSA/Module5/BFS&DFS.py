'''Implement graph using python programming with the followings:
Create a class vertex with the properties nodename and nextNode
Create a class neighbor with the properties Node and Next
Create a class graph with the data member start
Define a member function Add vertex to add vertices in the graph
Define a member function AddEdges to add neighboring nodes.
Define a member function BFS for traversal
Define a member function DFS for traversal
Define a member function Primes for finding shortest path'''
from collections import deque
import heapq

class Neighbor:
    def __init__(self, node_name, next_neighbor=None, weight=1):
        self.node = node_name  # name of the neighbor node
        self.next = next_neighbor
        self.weight = weight

class Vertex:
    def __init__(self, node_name):
        self.nodename = node_name
        self.nextNode = None   # linked list of other vertices
        self.neighbors = None  # head of neighbors linked list

class Graph:
    def __init__(self):
        self.start = None  # head of vertex list

    def find_vertex(self, name):
        current = self.start
        while current:
            if current.nodename == name:
                return current
            current = current.nextNode
        return None

    def add_vertex(self, name):
        if self.find_vertex(name):
            print(f"Vertex {name} already exists.")
            return
        new_vertex = Vertex(name)
        if not self.start:
            self.start = new_vertex
        else:
            current = self.start
            while current.nextNode:
                current = current.nextNode
            current.nextNode = new_vertex

    def add_edge(self, from_node, to_node, weight=1):
        from_vertex = self.find_vertex(from_node)
        to_vertex = self.find_vertex(to_node)
        if not from_vertex or not to_vertex:
            print(f"Either {from_node} or {to_node} does not exist.")
            return

        # Add neighbor to from_vertex
        new_neighbor = Neighbor(to_node, from_vertex.neighbors, weight)
        from_vertex.neighbors = new_neighbor

    def bfs(self, start_node):
        visited = set()
        queue = deque()
        queue.append(start_node)
        visited.add(start_node)

        print("BFS Traversal:", end=" ")
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            current_vertex = self.find_vertex(node)
            neighbor = current_vertex.neighbors
            while neighbor:
                if neighbor.node not in visited:
                    visited.add(neighbor.node)
                    queue.append(neighbor.node)
                neighbor = neighbor.next
        print()

    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        current_vertex = self.find_vertex(node)
        neighbor = current_vertex.neighbors
        while neighbor:
            if neighbor.node not in visited:
                self.dfs_util(neighbor.node, visited)
            neighbor = neighbor.next

    def dfs(self, start_node):
        visited = set()
        print("DFS Traversal:", end=" ")
        self.dfs_util(start_node, visited)
        print()

    def primes(self, start_node):
        # Dijkstra's algorithm (assumed to be the intent of "Primes")
        distances = {}
        for current in self.iter_vertices():
            distances[current.nodename] = float('inf')
        distances[start_node] = 0

        min_heap = [(0, start_node)]
        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)
            if curr_dist > distances[curr_node]:
                continue

            current_vertex = self.find_vertex(curr_node)
            neighbor = current_vertex.neighbors
            while neighbor:
                distance = curr_dist + neighbor.weight
                if distance < distances[neighbor.node]:
                    distances[neighbor.node] = distance
                    heapq.heappush(min_heap, (distance, neighbor.node))
                neighbor = neighbor.next

        print("Shortest path distances from", start_node)
        for node, dist in distances.items():
            print(f"{start_node} -> {node} = {dist}")

    def iter_vertices(self):
        current = self.start
        while current:
            yield current
            current = current.nextNode

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B", 1)
g.add_edge("A", "C", 4)
g.add_edge("B", "C", 2)
g.add_edge("C", "D", 1)

g.bfs("A")
g.dfs("A")
g.primes("A")
