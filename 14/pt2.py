filename = "input.txt"
# filename = "example.txt"

def next_pos(curr, rocks, lowpoint):
	full = rocks
	if(curr[1] == lowpoint-1): return curr
	if (curr[0], curr[1]+1) in full:
		if (curr[0]-1,curr[1]+1) in full:
			if (curr[0]+1,curr[1]+1) in full:
				return curr
			else:
				return (curr[0]+1,curr[1]+1)
		else:
			return (curr[0]-1,curr[1]+1)
	else:
		return (curr[0], curr[1]+1)

spawn = (500,0)
rock = set()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		steps = line.split(" -> ")
		current = steps[0].split(",")
		current = list(map(lambda x: int(x), current))
		for s in steps[1:]:
			nxt = s.split(",")
			nxt = list(map(lambda x: int(x), nxt))
			if(current[0] != nxt[0]):
				start = current[0]
				end = nxt[0]
				if(start > end):
					end = current[0]
					start = nxt[0]
				for p in range(start, end+1):
					rock.add((p, current[1]))
			elif(current[1] != nxt[1]):
				start = current[1]
				end = nxt[1]
				if(start > end):
					end = current[1]
					start = nxt[1]
				for p in range(start, end+1):
					rock.add((current[0], p))
			current=nxt
		line = f.readline().strip()

lowpoint = max(map(lambda x: x[1], rock))+2
full = False
count = 0

while(not full):
	grain = (spawn[0], spawn[1])
	count += 1
	resting = False
	while(not resting and not full):
		# print(grain)
		nxt = next_pos(grain, rock, lowpoint)
		if(nxt == grain):
			resting = True
			rock.add(grain)
		else: grain = nxt
		if(grain==spawn): full=True

print(count)
