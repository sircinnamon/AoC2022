import math
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
	positions = set()
	for y, row in enumerate(rock):
		for x, unit in enumerate(row):
			if(unit):positions.add((spawn[0]+x, spawn[1]-y))
	return positions

def detect_collisions(tower, positions):
	if(len(tower.intersection(positions))>0): return True
	for p in positions:
		if(p[0]<0 or p[0]>6): return True # Wall collide
		if(p[1]<0):return True
	return False

def shift_positions(positions, direction, mul=1):
	dirs = {
		">": (1,0),
		"<": (-1,0),
		"^": (0,1),
		"V": (0,-1),
	}
	mod = dirs[direction]
	out = set(map(lambda x: (x[0]+(mod[0]*mul), x[1]+(mod[1]*mul)), positions))
	return out

def has_full_line(tower, height):
	for i in range(7):
		if (i, height) not in tower:
			return False
	print("FULL LINE")
	return True

def cleanup_tower(tower, height):
	new_tower = set()
	for p in tower:
		if p[1] >= height:
			new_tower.add(p)
	return new_tower

def get_top_rows(tower, thickness = 20):
	# Get the top rows as a pattern
	outset = list()
	top = get_highest_point(tower)
	for p in tower:
		if(p[1] > top - thickness):
			outset.append((p[0],(p[1]-top)+thickness))
	return str(outset)

moves = list()
tower = set()

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		moves = list(line)
		line = f.readline().strip()

current_move = 0
history = dict()
# for r in range(2022):
r = 0
round_limit = 1000000000000
skipped = False
while r < round_limit:
	rock = rocks[r%5]
	rock_spawn = (2, 3+get_highest_point(tower)+len(rock))
	rock_pos = get_positions(rock, rock_spawn)
	drops = 0
	# print(rock_pos)
	# print_tower(tower, rock_pos)
	settled = False
	while not settled:
		new_pos = shift_positions(rock_pos, moves[current_move])
		current_move = (current_move + 1)%len(moves)
		if(not detect_collisions(tower, new_pos)):
			rock_pos = new_pos
		new_pos = shift_positions(rock_pos, "V")
		drops += 1
		if(drops <= 3): rock_pos = new_pos
		elif(not detect_collisions(tower, new_pos)):
			rock_pos = new_pos
		else:
			settled = True
	for p in rock_pos:
		tower.add(p)
	if(r % 500 == 0):
		highest = get_highest_point(tower)
		tower = cleanup_tower(tower, highest-50)
		if(r % 100000 == 0):print("*", end="", flush=True)
	state = (get_top_rows(tower), r%5, current_move-1)
	status = (r, get_highest_point(tower), current_move-1)
	if(not skipped and state in history):
		# Find a loop that has repeated >4 times
		if(len(history[state])>3):
			print("WEAK LOOP")
			diff1 = history[state][-3][0]-history[state][-4][0]
			hdiff1 = history[state][-3][1]-history[state][-4][1]
			diff2 = history[state][-2][0]-history[state][-3][0]
			hdiff2 = history[state][-2][1]-history[state][-3][1]
			diff3 = history[state][-1][0]-history[state][-2][0]
			hdiff3 = history[state][-1][1]-history[state][-2][1]
			# Ensure loop is stable
			if(diff1 == diff2 == diff3 and hdiff1 == hdiff2 == hdiff3):
				print("STRONG LOOP")
				print(diff1, diff2, diff3)
				print(hdiff1, hdiff2, hdiff3)
				print(state)
				print(status)
				skipped = True
				tower = cleanup_tower(tower, highest-50)
				skip_count = math.floor((round_limit-r)/diff1)
				print("reapeat x",skip_count)
				# Repeat loop as close to limit as possible
				r+=(diff1*skip_count)
				tower = shift_positions(tower, "^", mul=(hdiff1*skip_count))

		history[state].append(status)
	else:
		history[state] =list([status])
	r+=1

# print_tower(tower, rock)
print(get_highest_point(tower)+1)

