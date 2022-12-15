import re
filename = "input.txt"
# filename = "example.txt"

def manhattan(p1, p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

beacons = set()
sensors = list()
rex = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+).*')
check_height=2000000
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

rg = range(min_x-min_x_rad, max_x+max_x_rad)
blocked = 0
for x in rg:
	pos = (x, check_height)
	if(pos in beacons): continue
	else:
		for s in sensors:
			if(manhattan(pos, s["pos"]) <= s["radius"]):
				blocked+=1
				# print(pos, s, manhattan(pos, s["pos"]))
				break
print(blocked)