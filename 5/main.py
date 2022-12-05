import re
from collections import deque

filename = "input.txt"
building_piles = True
piles = deque()
with open(filename, "r") as f:
	line = f.readline().replace("\n", "")
	while line:
		if "[" in line:
			line = line.replace("    ", "[] ")
			crates = re.findall(r'\[(.?)\]', line)
			for i,v in enumerate(crates):
				if(i>=len(piles)): piles.append(deque())
				if(v!=""): piles[i].append(v)
		line = f.readline().replace("\n", "")
	line = f.readline().replace("\n", "")
	# print(piles)
	while line:
		if "move" in line:
			regexmatch = re.match(r'move (\d+) from (\d+) to (\d+)', line)
			count = int(regexmatch[1])
			src = int(regexmatch[2])-1
			dest = int(regexmatch[3])-1
			for i in range(count):
				piles[dest].appendleft(piles[src].popleft())
		line = f.readline().replace("\n", "")
# print(piles)
print("".join([p[0] for p in piles]))