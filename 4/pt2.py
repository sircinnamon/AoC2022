filename = "input.txt"
counter=0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		ass = [list(map(lambda x: int(x), x.split("-"))) for x in line.split(",")]
		if (len(set(range(ass[0][0], ass[0][1]+1)) & set(range(ass[1][0], ass[1][1]+1))) > 0):
			counter += 1
		line = f.readline().strip()
print(counter)