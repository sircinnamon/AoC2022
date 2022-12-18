filename = "input.txt"
# filename = "example.txt"

rocks = list([
	[[1,1,1,1]],
	[[0,1,0],[1,1,1],[0,1,0]],
	[[0,0,1],[0,0,1],[1,1,1]],
	[[1],[1],[1],[1]],
	[[1,1],[1,1]]
])

def get_highest_point(tower):
	highest = -1
	for p in tower:
		if p[1] > highest: highest = p[1]
	return highest

def print_tower(tower, rock):
	st = list()
	for l in range(get_highest_point(tower)+7):
		line = ""
		for i in range(7):
			if((i,l) in tower): line+="#"
			elif((i,l) in rock): line+="@"
			else: line+="."
		line = "|"+line+"|"
		st.insert(0, line)
	print("\n".join(st))
	print("_________")

def get_positions(rock, spawn):
	positions = list()
	for y, row in enumerate(rock):
		for x, unit in enumerate(row):
			if(unit):positions.append((spawn[0]+x, spawn[1]-y))
	return positions

def detect_collisions(tower, positions):
	for p in positions:
		if p in tower: return True # Rock collide
		if(p[0]<0 or p[0]>6): return True # Wall collide
		if(p[1]<0):return True
	return False

def shift_positions(positions, direction):
	dirs = {
		">": (1,0),
		"<": (-1,0),
		"^": (0,1),
		"V": (0,-1),
	}
	mod = dirs[direction]
	out = list(map(lambda x: (x[0]+mod[0], x[1]+mod[1]), positions))
	return out

moves = list()
tower = set()

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		moves = list(line)
		line = f.readline().strip()

current_move = 0
# for r in range(2022):
for r in range(2022):
	rock = rocks[r%5]
	rock_spawn = (2, 3+get_highest_point(tower)+len(rock))
	rock_pos = get_positions(rock, rock_spawn)
	# print(rock_pos)
	# print_tower(tower, rock_pos)
	settled = False
	while not settled:
		new_pos = shift_positions(rock_pos, moves[current_move])
		current_move = (current_move + 1)%len(moves)
		if(not detect_collisions(tower, new_pos)):
			rock_pos = new_pos
		new_pos = shift_positions(rock_pos, "V")
		if(not detect_collisions(tower, new_pos)):
			rock_pos = new_pos
		else:
			settled = True
	for p in rock_pos:
		tower.add(p)

# print_tower(tower, rock)
print(get_highest_point(tower)+1)

