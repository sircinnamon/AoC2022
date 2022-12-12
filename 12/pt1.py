import math
filename = "input.txt"
# filename = "example.txt"

class Node:
	def __init__(self, height, text):
		self.height = height
		self.text = text
		self.edges = list()
		self.distanceFromStart = math.inf

	def __str__(self):
		return "{} (height: {}) (dist: {}) -> {}".format(self.text, self.height, self.distanceFromStart,[x.text for x in self.edges])

	def addEdge(self, node):
		if(node not in self.edges):
			self.edges.append(node)

	def addEdgeIfClimbable(self, node):
		if(node.height <= self.height+1):
			self.addEdge(node)

grid = list()
startNode = None
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		row = list()
		for n in list(line):
			height = ord(n)-ord("a")
			if n == "S":
				height = 0
			elif n == "E":
				height = ord("z")-ord("a")
			node = Node(height, n)
			if n == "S":
				startNode = node
				node.distanceFromStart = 0
			row.append(node)
		grid.append(row)
		line = f.readline().strip()

# Build edges
for row_ind, row in enumerate(grid):
	for col_ind, node in enumerate(row):
		# left
		if(col_ind > 0):
			node.addEdgeIfClimbable(grid[row_ind][col_ind-1])
		# right
		if(col_ind < len(grid[0])-1):
			node.addEdgeIfClimbable(grid[row_ind][col_ind+1])
		# up
		if(row_ind > 0):
			node.addEdgeIfClimbable(grid[row_ind-1][col_ind])
		# down
		if(row_ind < len(grid)-1):
			node.addEdgeIfClimbable(grid[row_ind+1][col_ind])
		# print(node)

# Djikstras
unvisited = list()
for row in grid: unvisited = unvisited+row
current = startNode
while(current.text != "E"):
	unvisited.remove(current)
	for neightbor in current.edges:
		if neightbor.distanceFromStart > current.distanceFromStart+1:
			neightbor.distanceFromStart = current.distanceFromStart+1
	nxt = unvisited[0]
	for n in unvisited:
		if n.distanceFromStart<nxt.distanceFromStart:
			nxt=n
	current = nxt
print(current)
