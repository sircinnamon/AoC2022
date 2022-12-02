filename = "input.txt"
total_score = 0
vals = ["A","B","C"]
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		o = line.split(" ")[0]
		o = vals.index(o)
		outcome = line.split(" ")[1]
		if(outcome == "Y"): total_score += 3 + o+1
		else:
			if(outcome=="Z"): total_score += 6+((o+1)%3)+1
			else: total_score += ((o-1)%3)+1
		line = f.readline().strip()

print(total_score) # part 2