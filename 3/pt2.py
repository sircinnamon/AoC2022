filename = "input.txt"
total_prio = 0

def prio(x):
	val = ord(list(x)[0])-96
	if(val < 0): val += 58
	return val

with open(filename, "r") as f:
	group = [set(f.readline().strip()), set(f.readline().strip()), set(f.readline().strip())]
	while group[0]:
		# print(group)
		common = group[0].intersection(group[1]).intersection(group[2])
		total_prio += prio(list(common)[0])
		group = [set(f.readline().strip()), set(f.readline().strip()), set(f.readline().strip())]

print(total_prio) # part 2