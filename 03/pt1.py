filename = "input.txt"
total_prio = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		halves = (set(line[:int(len(line)/2)]), set(line[int(len(line)/2):]))
		common = halves[0].intersection(halves[1])
		val = ord(list(common)[0])-96
		if(val < 0): val += 58
		total_prio += val
		line = f.readline().strip()

print(total_prio) # part 1