import re
filename = "input.txt"
# filename = "example.txt"

def manhattan(p1, p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

beacons = set()
sensors = list()
rex = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+).*')
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		pos = rex.search(line)
		beacon = (int(pos[3]), int(pos[4]))
		sens_pos = (int(pos[1]), int(pos[2]))
		rad = manhattan(sens_pos, beacon)
		sensor = {
			"pos": sens_pos,
			"beacon": beacon,
			"radius": rad
		}
		# print(pos[1], pos[2], pos[3], pos[4])
		# print(manhattan((int(pos[1]), int(pos[2])), (int(pos[3]),int(pos[4]))))
		beacons.add(beacon)
		sensors.append(sensor)
		line = f.readline().strip()

min_x = min([x["pos"][0] for x in sensors])
min_x_rad = [x["radius"] for x in sensors if x["pos"][0]==min_x][0]
max_x = max([x["pos"][0] for x in sensors])
max_x_rad = [x["radius"] for x in sensors if x["pos"][0]==max_x][0]

search_range = 4000001
# search_range = 21
def check_point(pt, sensors, beacons, search_range):
	if(pt in beacons): return False
	if(pt[0] not in range(search_range) or pt[1] not in range(search_range)):
		return False
	for s in sensors:
		if(manhattan(pt, s["pos"]) <= s["radius"]):
			return False
	return True

def get_edge(pt, radius):
	edge_points = list()
	rel = (0, radius+1)
	while(rel[1]>=0):
		edge_points.append((pt[0]+rel[0], pt[1]+rel[1]))
		rel = (rel[0]+1,rel[1]-1)
	rel = (rel[0]-1,rel[1]-1)
	while(rel[0]>=0):
		edge_points.append((pt[0]+rel[0], pt[1]+rel[1]))
		rel = (rel[0]-1,rel[1]-1)
	rel = (rel[0]-1,rel[1]+1)
	while(rel[1]<=0):
		edge_points.append((pt[0]+rel[0], pt[1]+rel[1]))
		rel = (rel[0]-1,rel[1]+1)
	rel = (rel[0]+1,rel[1]+1)
	while(rel[1]<0):
		edge_points.append((pt[0]+rel[0], pt[1]+rel[1]))
		rel = (rel[0]+1,rel[1]+1)
	return(edge_points)

for s in sensors:
	# Walk radius edge
	border = get_edge(s["pos"], s["radius"])
	for point in border:
		if(check_point(point, sensors, beacons, search_range)):
			# print(point)
			print(4000000*point[0] + point[1])
			quit()