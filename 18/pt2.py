filename = "input.txt"
# filename = "example.txt"

def count_faces(cubes, c):
	exposed = 0
	if((c[0],c[1],c[2]+1) not in cubes): exposed+=1
	if((c[0],c[1],c[2]-1) not in cubes): exposed+=1
	if((c[0],c[1]+1,c[2]) not in cubes): exposed+=1
	if((c[0],c[1]-1,c[2]) not in cubes): exposed+=1
	if((c[0]+1,c[1],c[2]) not in cubes): exposed+=1
	if((c[0]-1,c[1],c[2]) not in cubes): exposed+=1
	return exposed

def is_bubble(cubes, space):
	# Have to handle multi-space bubbles
	if(space in bubbles): return True
	if(space in cubes): return False
	if(is_enclosed(cubes, list([space]), set())): bubbles.add(space);return True
	return False

def is_enclosed(cubes, search, searched):
	maxes = get_max_dimensions(cubes)
	while len(search) > 0:
		# print(len(search), len(searched))
		if(len(searched)>len(cubes)): return False
		s = search.pop(0)
		# print(s)
		adj = set([
			(s[0]+1,s[1],s[2]),
			(s[0]-1,s[1],s[2]),
			(s[0],s[1]+1,s[2]),
			(s[0],s[1]-1,s[2]),
			(s[0],s[1],s[2]+1),
			(s[0],s[1],s[2]-1)
		])
		for a in list(adj):
			if(a in searched or a in cubes): adj.remove(a)
		searched.add(s)
		for a in adj:
			if a not in search: search.append(a)
			if(a[0] > maxes[0]): return False
			if(a[1] > maxes[1]): return False
			if(a[2] > maxes[2]): return False
	for s in searched:
		bubbles.add(s)
	return True

def get_max_dimensions(cubes):
	xs = max([c[0] for c in cubes])
	ys = max([c[1] for c in cubes])
	zs = max([c[2] for c in cubes])
	return (xs, ys, zs)


def count_exterior_faces(cubes, c):
	exposed = 0
	adj = (c[0],c[1],c[2]+1)
	if(adj not in cubes and not is_bubble(cubes, adj)): exposed+=1
	adj = (c[0],c[1],c[2]-1)
	if(adj not in cubes and not is_bubble(cubes, adj)): exposed+=1
	adj = (c[0],c[1]+1,c[2])
	if(adj not in cubes and not is_bubble(cubes, adj)): exposed+=1
	adj = (c[0],c[1]-1,c[2])
	if(adj not in cubes and not is_bubble(cubes, adj)): exposed+=1
	adj = (c[0]+1,c[1],c[2])
	if(adj not in cubes and not is_bubble(cubes, adj)): exposed+=1
	adj = (c[0]-1,c[1],c[2])
	if(adj not in cubes and not is_bubble(cubes, adj)): exposed+=1
	return exposed

cubes = set()
bubbles = set()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		c = [int(x) for x in line.split(",")]
		cubes.add((c[0], c[1], c[2]))
		line = f.readline().strip()

total = 0
for cube in cubes:
	total+= count_exterior_faces(cubes, cube)
# print(len(bubbles))
print(total)