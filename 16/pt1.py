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

def search_route(valves, curr, opened, minutes_remaining):
	options = list([0])
	# print("STATUS", curr, minutes_remaining)
	# print(len(opened), minutes_remaining)
	if(minutes_remaining <= 0): return 0
	if(curr not in opened):
		# print("Opening {} on {} releases {}".format(curr, minutes_remaining, valves[curr].flow*(minutes_remaining-1)))
		max_vent = valves[curr].flow*(minutes_remaining-1)+search_route(valves, curr, opened+[curr], minutes_remaining-1)
		return(max_vent)
		options.append(max_vent)
	for adj_v in valves:
		if adj_v not in opened and adj_v != curr:
			# walk there
			new_mins = minutes_remaining-(valves[curr].distances[adj_v])
			max_vent = 0
			if(new_mins>=0): max_vent = search_route(valves, adj_v, opened, new_mins)
			options.append(max_vent)
	return(max(options))

time_limit = 30
print("AA", search_route(important_valves, "AA", list(["AA"]), time_limit)) 