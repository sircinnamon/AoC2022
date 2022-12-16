import re
filename = "input.txt"
# filename = "example.txt"

def node_distance(valves, start, end):
	search = list([(start,0)])
	checked = list()
	while(len(search)>0):
		current, distance = search.pop(0)
		if(current == end):
			return distance
		checked.append(current)
		for adj in valves[current].connections:
			if(adj not in checked):
				search.append((adj, distance+1))
	return -1


class Valve:
	def __init__(self, name, flow, connections):
		self.name = name
		self.flow = flow
		self.connections = connections
		self.distances = {}
		self.distances[self.name] = 0

	def __str__(self):
		return "{} ({}) -> {}".format(self.name, self.flow, self.distances)

	def add_distance(self, node, dist):
		self.distances[node] = dist

valves = {}
important_valves = {}
rex = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		parse = rex.search(line)
		v = Valve(parse[1], int(parse[2]), parse[3].split(", "))
		valves[v.name] = v
		if(v.flow > 0): important_valves[v.name] = v
		line = f.readline().strip()

important_valves["AA"] = valves["AA"]

ivs = list(important_valves.values())
for i,v in enumerate(ivs):
	for adj_v in ivs[i+1:]:
		# print("{} to {}".format(v.name, adj_v.name))
		distance = node_distance(valves, v.name, adj_v.name)
		v.add_distance(adj_v.name, distance)
		adj_v.add_distance(v.name, distance)

# for iv in ivs: print(iv)

def search_route(valves, start, visited, time_remaining):
	if(time_remaining<=0):
		return (0, visited)
	if(len(visited) == len(valves)):
		return (0, visited)
	score = valves[start].flow * time_remaining
	options = list()
	for v in valves:
		if(v not in visited and v != start):
			options.append(search_route(
				valves,
				v,
				visited + [start],
				time_remaining - (valves[v].distances[start]+1)
			))
	if(len(options) == 0):
		return (score, visited+[start])
	options.sort(key=lambda x: x[0], reverse=True)
	return (score+options[0][0], options[0][1])

time_limit = 26

my_route = search_route(
	important_valves,
	"AA",
	list(),
	time_limit
)
# print(my_route)

el_route = search_route(
	important_valves,
	"AA",
	list(my_route[1]),
	time_limit
)
# print(el_route)
print(my_route[0]+el_route[0])