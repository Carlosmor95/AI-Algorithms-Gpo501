# Dijkstra algorithm: Find the shortest path between two nodes in a graph

import heapq

def solve(graph, startNode, endNode):
    # Set shortest distances from the start node to all other nodes as infinity
    distances = {node: float('infinity') for node in graph}
    distances[startNode] = 0

	# Set previous nodes for each node as None
    previousNodes = {node: None for node in graph}

	# Create a priority queue and add start node
    priorityQueue = [(0, startNode)]
    while priorityQueue:
        # Pop node with the smallest distance
        currentDistance, currentNode = heapq.heappop(priorityQueue)

		# If current node is the end node, return the path,
		# as the shortest path has been found
        if currentNode == endNode:
            path = []
            # Build shortest path by going backwards from end node
            while currentNode is not None:
                path.append(currentNode)
                currentNode = previousNodes[currentNode]
            
            # Reverse to order from start to end nodes
            path = path[::-1] # Python moment
            return path

		# If current distance is greater than the distance to current node, skip!
        if currentDistance > distances[currentNode]:
            continue
		
        for neighbor, weight in graph[currentNode].items():
            # Calculate the distance from the start node to the neighbor node
            distance = currentDistance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance # Update distance to neighbor
                previousNodes[neighbor] = currentNode # Update previous node of neighbor
                heapq.heappush(priorityQueue, (distance, neighbor)) # Add neighbor to priority queue

    return None

# Test request body
"""
{
    "graph": {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1}
    },
    "startNode": "A",
    "endNode": "D"
}
"""