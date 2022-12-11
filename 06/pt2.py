filename = "input.txt"
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		for i in range(14, len(line)):
			segment = line[i-14:i]
			if(len(set(segment)) == 14):
				print("{} at {}".format(segment, i))
				quit()
		line = f.readline().strip()