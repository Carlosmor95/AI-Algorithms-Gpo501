from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to the graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find the set of an element i
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does the union of two sets of x and y
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
        result = []  # This will store the resultant MST
        i = 0  # An index variable used for sorted edges
        e = 0  # An index variable used for the result[]

        # Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is less than V-1
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause a cycle, include it in the result
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree Weight:", minimumCost)
        return result


@app.route('/mst', methods=['POST'])
def calculate_mst():
    data = request.get_json()
    g = Graph(data['V'])
    for edge in data['edges']:
        g.addEdge(edge[0], edge[1], edge[2])
    mst = g.KruskalMST()
    # Construct a response JSON
    response_data = {
        "edges": mst,
        "minimum_weight": sum(weight for _, _, weight in mst)
    }

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
